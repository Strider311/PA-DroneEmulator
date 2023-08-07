import pika
import logging


class BaseQueueSender():
    def __init__(self, queue_name: str, rmq_host: str, name: str) -> None:
        self.queue_name = queue_name
        self.rmq_host = rmq_host
        self.name = name
        self.__init_logger__()

        connection_result = self.__connect__()
        if (connection_result == False):
            raise ConnectionError("Failed to connect to message broker")

        self.logger.info(f"Successfully connected to queue: {self.queue_name}")

    def __init_connection__(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.rmq_host))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def __init_logger__(self):
        logging.getLogger("pika").setLevel(logging.FATAL)
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

    def __connect__(self) -> bool:
        retry = 0
        max_retry = 5
        while (True):
            try:
                if (retry == max_retry):
                    return False

                self.__init_connection__()
                return True

            except Exception:
                retry += 1
                self.logger.warn(
                    f"Unable to communicate with message broker, retrying... {retry}")

    def send(self, message):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=message)
