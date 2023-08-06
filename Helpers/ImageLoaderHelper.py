import os
import rasterio
from Enums.ImageTypeEnum import ImageType
import logging
from Modules.DirectoryManager import DirectoryManager


class ImageLoaderHelper():

    def __init__(self):
        self.__init_directories__()
        logging.getLogger("rasterio").setLevel(logging.WARNING)

    def __init_directories__(self):
        self.directories = DirectoryManager.get_input_dirs()

    def load(self, file_name: str, image_type: ImageType):

        try:
            base_path = self.__get_base_path__(image_type)
            file = os.path.join(
                base_path, file_name)
            image = rasterio.open(file)
            return image.read(1).astype('float64')
        except Exception:
            raise ValueError("Unable to load file")

    def __get_base_path__(self, image_type: ImageType) -> str:

        match image_type:
            case ImageType.red:
                return self.directories["RED"]
            case ImageType.green:
                return self.directories["GREEN"]
            case ImageType.nir:
                return self.directories["NIR"]
            case ImageType.red_edge:
                return self.directories["RED_EDGE"]

            case _:
                raise ValueError("Invalid image type")
