import asyncio
from abc import ABCMeta, abstractmethod
import importlib
import logging
from godeye_agent import config
import aiohttp

logger = logging.getLogger(__name__)


class AbstractNetworkChecker(metaclass=ABCMeta):

    @asyncio.coroutine
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError('AbtractNetworkChecker cant call')


class NetworkChecker(AbstractNetworkChecker):
    def __init__(self):
        self._load_plugins()

    def _load_plugins(self):
        path = config.enable_plugin[0]['path']
        name = config.enable_plugin[0]['name']
        plugin = importlib.import_module(path, __name__)
        self.plugin = getattr(plugin, name)

    def __call__(self, client):
        try:
            with aiohttp.Timeout(config.check_timeout):
                r = yield from self.plugin()

                logger.info('Network checker')
                return r
        except asyncio.TimeoutError:
            logger.info('################################'
                        '###################None')
            return None
