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


class Download(AbstractCheckPlugin):

    @asyncio.coroutine
    def __call__(self, client, node_target):
        logger.info('Test download speed :  running...')
        result = yield from self.get_result(node_target)
        yield from self._queue.put(result)

    @asyncio.coroutine
    def get_result(self, result):
        """
        download and processing data
        """
      localFilename = url.split('/')[-1]
      start = time.clock()
      r = requests.get(url, stream=True)
      total_length = int(r.headers.get('content-length'))
      if total_length is None:
        logger.info("Test download speed : done!")
        pass
      else:
        array_speed = []
        start_chunk = time.clock()
        for chunk in r.iter_content(1024): # 1kB1024 1MB 1048576
          end_chunk = time.clock()
          delta = end_chunk - start_chunk
          start_chunk = end_chunk
          if delta <= 0:
            pass
          else:
             array_speed.append(1//delta) # kB / s
        print array_speed

        # caculate
        download_speed = total_length // (time.clock() - start)
        acceleration = self.acceleration(array_speed)
        mean_deviation = self.mean_deviation(array_speed, download_speed)
      logger.info("Test download speed done!")
      return [download_speed, mean_deviation, acceleration, str(datetime.now())]

    def acceleration(array_speed):
      if len(array_speed) == 0:
        return []
      speed_before = array_speed[0]
      for speed in array_speed:
        if speed < speed_before:
          break
        else:
          speed_before = speed
      
      return speed_before - array_speed[0]

    def mean_deviation(array_speed, download_speed):
      if len(array_speed) == 0:
        return []
      sum = 0
      for speed in array_speed:
        sum += abs(speed - download_speed)

      return sum//len(array_speed)
