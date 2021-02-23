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

    source_news = get_sources()
    article = get_article(id)
    return render_template('article.html',news = source_news, article = article)

@main.route('/category/<tab>')
def category(tab):

    source_news = get_sources()
    category = get_category(tab)
    return render_template('category.html',news = source_news , category = category)