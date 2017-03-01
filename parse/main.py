import html2markdown
from bs4 import BeautifulSoup
import requests
import json
import html2markdown
context = requests.get('http://www.graphadvantage.com/real-time-neo4j-graph-updates-using-kafka-messaging/')

if context:
    text = BeautifulSoup(context.content,'html.parser')
    text = text.article.find_all(recursive = False)
    text = text[1].find_all()
    text = text[4]
    #import ipdb; ipdb.set_trace()
    
    # text = text.find_all()[0]
    print html2markdown.convert(text)
