import asyncio
from abc import ABCMeta, abstractmethod


class AbstractCheckPlugin(metaclass=ABCMeta):
    @asyncio.coroutine
    @abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError('Base_Plugin cant call')
