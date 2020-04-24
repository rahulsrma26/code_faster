import re
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

from .base_fetcher import BaseFetcher


class CodeForceFetcher(BaseFetcher):

    PATTERNS = {
        'contest': re.compile("contest/([a-zA-Z0-9]+)/problem/([A-G])"),
        'problem': re.compile("problem/([a-zA-Z0-9]+)/([A-G])")
    }

    def dirname(self):
        problem, level = None, None
        for pattern in self.PATTERNS.values():
            match = pattern.search(self.url)
            if match:
                problem = match.group(1)
                level = match.group(2)
                return 'CF{}-{}'.format(problem, level)


    def tests(self):
        if not self.text:
            return

        soup = BeautifulSoup(self.text, 'html.parser')

        previous = None
        for div in soup.find_all('div', {'class': 'sample-test'}):
            # print('s', div.get_text())
            inp = div.find("div", {"class": "input"}).find("pre")
            out = div.find("div", {"class": "output"}).find("pre")
            yield inp.get_text(), out.get_text()
            # dtype = div['class'][0]
            # text = div.find('pre').get_text()
            # if text[0] == '\n':
            #     text = text[1:]
            # if dtype == 'input':
            #     previous = text
            # elif dtype == 'output':
            #     yield previous, text
