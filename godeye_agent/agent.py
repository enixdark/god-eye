import sys
import logging
import asyncio
from godeye_agent import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from godeye_agent.networkchecker import NetworkChecker
import aiohttp
from datetime import datetime

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

@asyncio.coroutine
def tick(dsf):
    print('Tick! The time is: %s' % datetime.now())


class Agent(object):
    def __init__(self, _client):
        self.network_checker = NetworkChecker()
        self.scheduler = AsyncIOScheduler()
        self._add_job(_client)

    def _add_job(self, _client):
        # self.scheduler.add_job(tick, 'interval', seconds=config.check_interval, args=[_client,])
        self.scheduler.add_job(tick, 'interval', seconds=config.check_interval, args=[_client,])


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession() as client:
        _agent = Agent(client)
        _agent.scheduler.start()
    print('Press Ctrl+C to exit')

    # Execution will block here until Ctrl+C is pressed.
    try:
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
