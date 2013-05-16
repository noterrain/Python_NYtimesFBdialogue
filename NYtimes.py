from urllib2 import urlopen
from json import loads
import codecs
import time

def call_the_articles():
    #url = "http://api.nytimes.com/svc/search/v1/article?query=China&facets=publication&begin_date=19950101&end_date=20131231&api-key=bbab04af465c98391b73dcd9330fd969:1:66939014"
    url = "http://api.nytimes.com/svc/search/v1/article?query=China&begin_date=20120101&end_date=20131231&api-key=bbab04af465c98391b73dcd9330fd969:1:66939014"
    
    data= loads(urlopen(url).read())
    posts = list()
    for item in data["results"]:
            if'title' in item:
                 posts.append(item)
    return posts


if __name__ == '__main__':
    
	    
	for story in call_the_articles():
             print story['url'].encode('ascii', 'replace')