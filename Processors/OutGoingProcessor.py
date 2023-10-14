import json
from Modules.Messaging.NewImageSender import NewImageSender
from dto.NewImageDTO import NewImageDTO
import logging
from Modules.ImageReader import ImageReader
from Helpers.NumpyEncoder import NumpyEncoder


class OutGoingProcessor():

    def __init__(self) -> None:
        self.__init_logger__()
        self.new_image_publisher = NewImageSender()
        self.start()

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __callback__(self, image_dto: NewImageDTO):
        self.logger.info(f"Publishing new image: {image_dto.fileName}")
        json_dto = image_dto.get_json()
        json_dto: str = json.dumps(json_dto, cls=NumpyEncoder)
        self.new_image_publisher.publish_new_image(json_dto)

    def start(self):
        self.image_reader = ImageReader(self.__callback__)
        self.image_reader.start()
