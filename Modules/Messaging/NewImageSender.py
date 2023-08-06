from Modules.Messaging.BaseQueueSender import BaseQueueSender
from dto.NewImageDTO import NewImageDTO

import os


class NewImageSender(BaseQueueSender):

    def __init__(self) -> None:
        rmq_host = os.getenv("RMQ_HOST")
        queue_name = os.getenv("RMQ_NEW_IMAGE_NAME")
        name = "NewImageSender"
        super().__init__(queue_name, rmq_host, name)

    def publish_new_image(self, message: NewImageDTO):
        self.send(message=message)
