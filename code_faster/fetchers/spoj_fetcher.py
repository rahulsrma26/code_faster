from urllib.parse import urlsplit
from bs4 import BeautifulSoup

from .base_fetcher import BaseFetcher


class SPOJFetcher(BaseFetcher):

    def dirname(self):
        comps = urlsplit(self.url).path.split('/')
        return 'SPOJ-{}'.format(comps[2])

    def tests(self):
        print('As there is no standard HTML in SPOJ, test-case fetching is not supported.')
        yield from ()
