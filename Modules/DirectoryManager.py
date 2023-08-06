import os
import logging


class DirectoryManager():

    def __init__(self) -> None:

        self.logger = logging.getLogger(__name__)
        self.__init_directories__()

    def __init_directories__(self):

        self.image_folders = {
            "RED": os.getenv("RED_DIR"),
            "GREEN": os.getenv("GREEN_DIR"),
            "NIR": os.getenv("NIR_DIR"),
            "RED_EDGE": os.getenv("RED_EDGE_DIR")
        }

        self.__init_input_dir__()
        self.__init_output_dir__()

    def __init_input_dir__(self):
        self.input_dir = {}
        self.base_input_dir = os.getenv("ORIGINAL_DATA_DIR")

        for key in self.image_folders:
            self.input_dir[key] = os.path.join(
                self.base_input_dir, self.image_folders[key], "Train_Images")

    def __init_output_dir__(self):
        self.output_dir = {}
        self.base_output_dir = os.getenv("OUTPUT_BASE_PATH")

        if (os.path.exists(self.base_output_dir) == False):
            self.logger.info("Creating output directory")
            os.mkdir(self.base_output_dir)
        else:
            self.logger.info("Main output directory exists")

        for key in self.image_folders:
            temp_dir = os.path.join(
                self.base_output_dir, self.image_folders[key])

            self.output_dir[key] = temp_dir

            if (os.path.exists(temp_dir) == False):
                self.logger.info(
                    f"Creating {self.image_folders[key]} directory")
                os.mkdir(temp_dir)
            else:
                self.logger.info(
                    f"Output directory for {self.image_folders[key]} already exists")

    def get_output_dirs(self) -> dict():
        return self.output_dir

    def get_input_dirs(self) -> dict():
        return self.input_dir
