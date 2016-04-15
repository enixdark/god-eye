import asyncio
from abc import ABCMeta, abstractmethod
import importlib
import logging
from godeye_agent import config


logger = logging.getLogger(__name__)


class AbstractNetworkChecker(metaclass=ABCMeta):
    def __init__(self, client, loop):
        self._plugins = []
        self._client = client
        self._loop = loop
        self._load_plugins()


    def _load_plugins(self):
        for check in config.enable_plugin:
            name = check['name']
            path = check['path']
            try:
                plugin = self._load_plugin(name, path)
            except Exception as e:
                logger.info('Error: {!r}'.format(e))
                plugin = None
                raise e

            if plugin:
                self._plugins.append(plugin)


    def _load_plugin(self, name, path):
        plugin = importlib.import_module(path, __name__)
        return getattr(plugin, name)(self._loop)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError('AbtractNetworkChecker cant call')

    @asyncio.coroutine
    def real_call(self, node_target):
        if self._plugins:
            cors = [plugin(self._client, node_target) for plugin in self._plugins]
            r = asyncio.wait(cors, loop=self._loop)
            return r

        raise Exception('No Plugin')



class NetworkChecker(AbstractNetworkChecker):
    def __call__(self, get_node):
        logger.info('Network checker start running')
        node_target = get_node()
        future = asyncio.run_coroutine_threadsafe(self.real_call(node_target), self._loop)
        try:
            result = future.result(config.check_timeout)  # Wait for the result with a timeout
        except asyncio.TimeoutError:
            logger.info('The coroutine took too long, cancelling the task...')
            future.cancel()
        except Exception as exc:
            logger.info('The coroutine raised an exception: {!r}'.format(exc))
        else:
            logger.info('The coroutine returned: {!r}'.format(result))
            logger.info('Network checker end!!!')

