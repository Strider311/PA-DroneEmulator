from Modules.Messaging.NewImageSender import NewImageSender
from dto.NewImageDTO import NewImageDTO
import logging


class OutGoingProcessor():

    def __init__(self) -> None:
        self.new_image_sender = NewImageSender()
        self.__init_logger__()

    def __init_logger__(self):

        self.logger = logging.getLogger(f'Main.MainProcessor')
        self.logger.setLevel(logging.DEBUG)
