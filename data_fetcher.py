
""" Scrapes the web and caches data to disk for the Biased News Sentiment program.

    Written by Kyle Combes for Software Design (Spring 2017) Mini Project 3
    at Olin College of Engineering.
"""
import os.path
import requests
import untangle
import json
from bs4 import BeautifulSoup
from data_structures import *

class DataFetcher:

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    FILE_PREFIX = 'data/'

    def fetch_latest_from_feeds(sources):
        """ Fetches the latest article URLs for each source, downloads any new
            (not previously downloaded) articles, and caches the result to the disk.

            sources: a dictionary where the keys are shorthand names (& UIDs) for the sources
                    and the values are Source objects
            returns: the Sources object passed initially
        """

        # Check if any of the sources have cached data
        for src_name,src in sources.items():
            filename = '%s%s.json' % (DataFetcher.FILE_PREFIX, src_name)
            if os.path.isfile(filename):
                f = open(filename, 'r')
                json_str = f.read()
                f.close()
                json_obj = json.loads(json_str)
                loaded_src = NewsSentimentJSONDecoder().decode(json_obj)
                loaded_src.rss_url = src.rss_url # In case we want to change the URL
                loaded_src.name_full = src.name_full # In case we want to change the display name
                sources[src_name] = loaded_src
            else:
                # New source -- add it
                sources[src_name] = src

        # Get any new articles for each source
        for src_name,src in sources.items():
            recent_articles_from_feed = DataFetcher.fetch_articles_meta_from_feed(src)
            old_articles = src.articles
            print('Already have %i articles loaded for %s' % (len(old_articles), src_name))

            for recent_article in recent_articles_from_feed:
                if recent_article.url not in old_articles:
                    article = DataFetcher.fetch_rest_of_article(recent_article, src.content_class)
                    src.articles[recent_article.url] = article
                    print('Added new article:',recent_article.url)
                else:
                    print('Article %s already loaded. Not downloading again.' % recent_article.url)

            # Save the data
            src_as_json_obj = NewsSentimentJSONEncoder().default(src)
            filename = '%s%s.json' % (DataFetcher.FILE_PREFIX, src_name)
            f = open(filename, 'w')
            f.write(json.dumps(src_as_json_obj))
            f.close()

        return sources

    def fetch_rss_xml(source):
        """ Gets the RSS feed XML.

            source: a Source with the rss_url attribute set
            returns: an XML object
        """
        print('Fetching RSS XML from URL "%s"' % source.rss_url)
        xml_str = requests.get(source.rss_url, headers=DataFetcher.headers).text
        return untangle.parse(xml_str)

    def fetch_articles_meta_from_feed(source):
        """ Fetches the latest articles from a given RSS feed source.

            source: a Source with the url attribute defined
            returns: a list of Articles with the title and url attributes set
        """
        xml_obj = DataFetcher.fetch_rss_xml(source)
        print('XML fetched and parsed')
        articles = list()

        for elem in xml_obj.rss.channel.item:
            title = elem.title.cdata
            url = elem.link.cdata
            articles.append(Article(url, title))
        return articles

    def fetch_rest_of_article(article, content_class):
        """ Takes an Article with a URL specified and downloads the content.

            article: an Article with a defined url attribute
            content_class: the CSS class of the div containing the article content
            returns: the original Article with the text form the article loaded
                    into the 'content' variable
        """
        # Download the raw HTML
        try:
            r = requests.get(article.url)
            full_html = r.text
            bs = BeautifulSoup(full_html, 'lxml')
        except:
            print('Exception while trying to get data for %s.\nResponse code: %s' % (article.url, r.status_code))
            return

        # Pull out the article text
        content = bs.find('div', { 'class': content_class })
        if content:
            # Combine the text from all the paragraph tags into one string
            article.content = ' '.join([p.get_text() for p in content.find_all('p')])
        else:
            # Page is not an article (could be a video)
            article.content = ''
        return article
