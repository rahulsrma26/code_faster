from urllib.parse import urlsplit
from .cf_fetcher import CodeForceFetcher
from .spoj_fetcher import SPOJFetcher
from .cc_fetcher import CodeChefFetcher


class FetcherFactory:
    def __init__(self):
        self._fetchers = {}

    def register(self, key, fetcher):
        self._fetchers[key] = fetcher

    def get(self, url):
        key = urlsplit(url).netloc
        if key not in self._fetchers:
            raise ValueError(f'key "{key}" not found')
        return self._fetchers.get(key)(url)


factory = FetcherFactory()
factory.register('codeforces.com', CodeForceFetcher)
factory.register('www.spoj.com', SPOJFetcher)
factory.register('www.codechef.com', CodeChefFetcher)
