from flask import render_template
from . import main
from ..request import get_sources,get_article,get_headlines,get_category

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    source_news = get_sources()
    headlines = get_headlines()
    return render_template('index.html', news = source_news, headlines = headlines)

@main.route('/articles/<id>')
def article(id):
    '''
    articles page function that returns the articles page and its data
    '''

    source_news = get_sources()
    article = get_article(id)
    form = id.translate({ord('-'): None}).split(" ")
    id = " ".join(form).upper()
    return render_template('article.html',news = source_news, article = article,id=id)

@main.route('/category/<tab>')
def category(tab):
    '''
    Category page function that returns the category page and its data
    '''

    source_news = get_sources()
    category = get_category(tab)
    return render_template('category.html',news = source_news , category = category)