import asyncio
import aiohttp
import logging
from agent import config

logger = logging.getLogger(__name__)


class SendResult(object):
    def __init__(self, queue):
        self._queue = queue

    @asyncio.coroutine
    def __call__(self):
        """
        _queue chua coroutine cua

        :return:
        """

        # Neu Kien ko dung client cua aiohttp thi ko can dung dong nay.
        with aiohttp.ClientSession() as client:
            while True:
                cor_result = yield from self._queue.get()
                result = yield from cor_result
                logger.info(result)
                # CHo nay Kien viet ham gui data....


                # client.post(config.db_url, data=result)