import asyncio
from abc import ABCMeta, abstractmethod


class AbstractCheckPlugin(metaclass=ABCMeta):
    def __init__(self, loop):
        self._loop = loop

    @asyncio.coroutine
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError('Base_Plugin cant call')
