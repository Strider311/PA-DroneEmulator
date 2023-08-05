import os
import logging


class DirectoryManager():

    def __init__(self) -> None:

        self.output_base_path = os.getenv("DATA_BASE_PATH")
        self.image_output_dir = {
            "RED": os.getenv("RED_DIR"),
            "GREEN": os.getenv("GREEN_DIR"),
            "NIR": os.getenv("NIR_DIR"),
            "RED_EDGE": os.getenv("RED_EDGE_DIR")
        }

        self.logger = logging.getLogger('Main.DirectoryManager')

        self.__init_directories__()

    def __init_directories__(self):

        if (os.path.exists(self.output_base_path) == False):
            self.logger.info("Creating output directory")
            os.mkdir(self.output_base_path)
        else:
            self.logger.info("Main output directory exists")

        for key in self.image_output_dir:
            temp_dir = os.path.join(
                self.output_base_path, self.image_output_dir[key])

            if (os.path.exists(temp_dir) == False):
                self.logger.info(
                    f"Creating {self.image_output_dir[key]} directory")
                os.mkdir(temp_dir)
            else:
                self.logger.info(
                    f"Output directory for {self.image_output_dir[key]} already exists")
