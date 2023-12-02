import datetime
import os
import logging
from Enums.ImageTypeEnum import ImageType
from Modules.DirectoryManager import DirectoryManager
from dto.NewImageDTO import NewImageDTO


class ImageReader():

    def __init__(self, callback) -> None:
        self.__init_logger__()
        self.__read_directory__()
        self.callback = callback

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __read_directory__(self):
        self.input_path = os.getenv("ORIGINAL_DATA_DIR")
        self.images = os.listdir(self.input_path)

    def start(self):

        for image in self.images:
            image_dto = NewImageDTO(fileName=image,
                                    dt_processed=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                    path=self.input_path+ "\\" + image
                                    )

            self.callback(image_dto)
