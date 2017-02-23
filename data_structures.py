""" Data structures for the News Sentiment program.

    Written by Kyle Combes for Software Design (Spring 2017) Mini Project 3
    at Olin College of Engineering.
"""
import json

class Article:
    """ Stores article data """
    def __init__(self, url, title, content = None):
        self.url = url
        self.title = title
        self.content = content

class Source:
    """ Keeps track of articles associated with a source.

        Name is the name of the source, and articles is a dictionary of
        Article objects indexed by URL.
    """
    def __init__(self, name, name_full, rss_url, content_class):
        self.name = name
        self.name_full = name_full
        self.rss_url = rss_url
        self.content_class = content_class
        self.articles = {}


class NewsSentimentJSONEncoder(json.JSONEncoder):
    """ Encodes the objects defined in the beginning of this module as a JSON object. """

    def default(self, o):

        if isinstance(o, Article):
            return {'title':o.title, 'url':o.url, 'content':o.content}

        if isinstance(o, Source):
            enc = NewsSentimentJSONEncoder()
            articles_serialized = {n: enc.default(a) for n,a in o.articles.items()}
            return {'name':o.name, 'name_full':o.name_full, 'rss_url': o.rss_url, 'content_class': o.content_class,
                               'articles':articles_serialized}

        # Dictionary of sources
        if isinstance(o, dict) and isinstance(next(iter(o.values())),Source):
            enc = NewsSentimentJSONEncoder()
            return {name: enc.default(src) for name,src in o.items()}

        else:
            return json.JSONEncoder.default(self,o)

class NewsSentimentJSONDecoder:
    """ Decodes the objects defined in the beginning of this module stored as a JSON object. """

    def decode(self, o):
        # res = {}
        src_json = o
        src_name = o['name']
        # # For each source
        # for src_name, src_json in o.items():
        src_obj = Source(src_json['name'], src_json['name_full'], src_json['rss_url'], src_json['content_class'])
        # For each article
        for art_url, art_json in src_json['articles'].items():
            art = Article(art_json['url'], art_json['title'], art_json['content'])
            src_obj.articles[art_url] = art
        # res[src_name] = src_obj
        return src_obj #res
