class Source:
    '''
    Source class to define News Source Objects
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

class Article:
    '''
    Article class to define Article objects
    '''
    def __init__(self,description,urlToImage,publishedAt,url,title):
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
        self.title = title