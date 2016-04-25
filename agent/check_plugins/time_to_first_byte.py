import logging
import asyncio
from agent.check_plugins import AbstractCheckPlugin

# Do khong biet dung thu vien asyncio ntn ca nen em dung thu vien request
# python
import requests
import sys
import time
from datetime import datetime

logger = logging.getLogger(__name__)


class FirstByte(AbstractCheckPlugin):

    @asyncio.coroutine
    def __call__(self, client, node_target):
        logger.info('Caculating time for download first byte...')
        result = yield from self.get_result(node_target)
        yield from self._queue.put(result)

    @asyncio.coroutine
    def get_result(self, result):
        """
        download and processing data
        """
      localFilename = url.split('/')[-1]
      r = requests.get(url, stream=True)
      if total_length is None:
        logger.info("empty file!")
        return None
      else:
        start_chunk = time.clock()
        for chunk in r.iter_content(1024): # 1kB1024 1MB 1048576
          end_chunk = time.clock()
          break
        
        delta = end_chunk - start_chunk # time to first byte
        if delta <= 0:
          return None
        else:
          logger.info("Caculation time for download first byte done!")
          return [delta, str(datetime.now())]
           
      
