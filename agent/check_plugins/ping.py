import logging
import asyncio
import aiohttp
from godeye_agent.check_plugins import AbstractCheckPlugin

logger = logging.getLogger(__name__)


class Ping(AbstractCheckPlugin):
    @asyncio.coroutine
    def __call__(self, client, node_target):
        logger.info('Ping running...')
        r = yield from client.get(node_target)
        text = yield from r.text()
        logger.info('Ping result:' + text)
        return text


# Fast test =)))
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     with aiohttp.ClientSession() as client:
#         x = loop.run_until_complete(Ping()(client))
#     print(x)
#     print('Press Ctrl+C to exit')
#
#     # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
#     try:
#         loop.run_forever()
#     except (KeyboardInterrupt, SystemExit):
#         pass
