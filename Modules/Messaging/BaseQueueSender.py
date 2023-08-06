import pika
import logging


class BaseQueueSender():
    def __init__(self, queue_name: str, rmq_host: str, name: str) -> None:
        self.queue_name = queue_name
        self.rmq_host = rmq_host
        self.name = name
        self.__init_logger__()
        self.__connect__()

    def __init_connection__(self) -> None:
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.rmq_host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def __init_logger__(self):
        logging.getLogger("pika").setLevel(logging.FATAL)
        self.logger = logging.getLogger(f'Main.{self.name}')
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
        self.logger.info(f"Publishing new image: {message}")
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=message)
