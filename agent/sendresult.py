import asyncio
import logging
from influxdb import InfluxDBClient
from agent import config

logger = logging.getLogger(__name__)


class SendResult(object):

    def __init__(self, queue):
        self._queue = queue
        self.client = Connector.get_client()

    @asyncio.coroutine
    def __call__(self):
        """
        _queue chua coroutine cua

        :return:
        """

        # Neu Kien ko dung client cua aiohttp thi ko can dung dong nay.
        # with aiohttp.ClientSession() as client:
        while True:
            cor_result = yield from self._queue.get()
            result = yield from cor_result
            logger.info(result)
            if self.client is not None:
                self.client.write_points(result)
            else:
                raise Exception(
                    "We get some problems with database connection")


class Connector(object):

    def __init__(self):
        self.host = config.INFLUXDB_HOST
        self.port = config.INFLUXDB_PORT
        self.username = config.INFLUXDB_USERNAME
        self.password = config.INFLUXDB_PASSWORD
        self.database = config.INFLUXDB_DBPASSW

    def get_client(self):
        client = None
        try:
            client = InfluxDBClient(self.host, self.port, self.username,
                                    self.password, self.database)
        except Exception as err:
            print("Connect to InfluxDB failed, due to: ", err)
        return client
