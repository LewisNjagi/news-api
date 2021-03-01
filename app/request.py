import urllib.request,json
from .models import Source,Article


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    '''
    Function that gets news sources
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news source details

    Returns :
        source_results: A list of news source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        if id:
            source_object = Source(id,name,description)
            source_results.append(source_object)

    return source_results

def get_article(id):
    '''
    Function that gets news source articles by id of the news source
    '''
    get_source_article_url = 'http://newsapi.org/v2/everything?sources={}&sortBy=publishedAt&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_source_article_url) as url:
        source_article_data = url.read()
        source_article_response = json.loads(source_article_data)


        source_object = None
        if source_article_response['articles']:
            source_article_list = source_article_response['articles']
            source_object = process_get_article(source_article_list)

    return source_object

def process_get_article(article_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain movie details

    Returns :
        source_object: A list of news article objects
    '''
    source_object = []
    for article in article_list:
        description = article.get('description')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        url = article.get('url')
        title = article.get('title')

        if urlToImage and description:
            article_object = Article(description,urlToImage,publishedAt,url,title)
            source_object.append(article_object)

    return source_object

def get_headlines():
    '''
    Function that gets news source articles headlines
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&sortBy=publishedAt&apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_object = None
        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_object = process_get_article(get_headlines_list)

    return get_headlines_object

def get_category(tab):
    '''
    Function that gets news source articles headlines by category
    '''
    get_category_url = 'https://newsapi.org/v2/top-headlines?country=us&category={}&sortBy=publishedAt&apiKey={}'.format(tab,api_key)

    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_object = None
        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_object = process_get_article(get_category_list)

    return get_category_object