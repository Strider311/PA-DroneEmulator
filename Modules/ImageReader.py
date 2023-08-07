import datetime
import os
import logging
from Helpers.ImageLoaderHelper import ImageLoaderHelper
from Enums.ImageTypeEnum import ImageType
from dto.NewImageDTO import NewImageDTO


class ImageReader():

    def __init__(self, callback) -> None:
        self.__init_logger__()
        self.image_loader = ImageLoaderHelper()
        self.__read_directory__()
        self.callback = callback

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __load_image__(self, fileName, image_type):
        image = self.image_loader.load(fileName, image_type)
        return image

    def __read_directory__(self):
        self.input_paths = self.image_loader.dir_manager.get_input_dirs()
        self.images = os.listdir(self.input_paths["RED"])

    def start(self):

        for image in self.images:
            image_dto = NewImageDTO(fileName=image,
                                    green_image=self.image_loader.load(
                                        image, ImageType.green),
                                    red_image=self.image_loader.load(
                                        image, ImageType.red),
                                    nir_image=self.image_loader.load(
                                        image, ImageType.nir),
                                    red_e_image=self.image_loader.load(
                                        image, ImageType.red_edge),
                                    dt_processed=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                    )

            self.callback(image_dto)
