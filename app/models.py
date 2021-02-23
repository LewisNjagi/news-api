class Source:
    '''
    News class to define News Objects
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

class Article:
    def __init__(self,description,urlToImage,publishedAt,url):
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url