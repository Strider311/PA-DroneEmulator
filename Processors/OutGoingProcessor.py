from Modules.Messaging.NewImageSender import NewImageSender
from dto.NewImageDTO import NewImageDTO
import logging
from Helpers.ImageLoaderHelper import ImageLoaderHelper
import os


class OutGoingProcessor():

    def __init__(self) -> None:
        self.new_image_sender = NewImageSender()
        self.__init_logger__()
        self.image_loader = ImageLoaderHelper()

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __load_image__(self, fileName, image_type):
        image = self.image_loader.load(fileName, image_type)
        return image
