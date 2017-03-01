# import bs4
from bs4 import BeautifulSoup
import requests



_tags = ('main', 'article', 'section')
_attrs = ('id')
def get_link(uri):
    context = requests.get(uri)

    return context


def extract(html):
    bs = BeautifulSoup(html, 'html.parser')
    import ipdb; ipdb.set_trace()





