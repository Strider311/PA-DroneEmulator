import datetime
import os
import logging
from Enums.ImageTypeEnum import ImageType
from Modules.DirectoryManager import DirectoryManager
from dto.NewImageDTO import NewImageDTO
import uuid


class ImageReader():

    def __init__(self, callback) -> None:
        self.__init_logger__()
        self.dir_manager = DirectoryManager()
        self.__read_directory__()
        self.callback = callback

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __read_directory__(self):
        self.input_paths = self.dir_manager.get_input_dirs()
        self.images = os.listdir(self.input_paths["RED"])

    def start(self):

        for image in self.images:
            image_dto = NewImageDTO(fileName=image,
                                    dt_processed=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                    id=str(uuid.uuid4())
                                    )

            self.callback(image_dto)
