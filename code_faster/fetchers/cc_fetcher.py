from urllib.parse import urlsplit
from bs4 import BeautifulSoup

from .base_fetcher import BaseFetcher


class CodeChefFetcher(BaseFetcher):

    def dirname(self):
        comps = urlsplit(self.url).path.split('/')
        # print(comps)
        return 'CC-{}-{}'.format(comps[1], comps[3])

    def tests(self):
        print('As there is no standard HTML in CodeChef, test-case fetching is not supported.')
        yield from ()
