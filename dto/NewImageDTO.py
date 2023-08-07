from datetime import datetime


class NewImageDTO:

    def __init__(self,
                 fileName: str,
                 dt_processed: datetime,
                 red_image,
                 nir_image,
                 green_image,
                 red_e_image,
                 ):
        self.fileName = fileName
        self.dt_processed = dt_processed
        self.red_image = red_image
        self.nir_image = nir_image
        self.green_image = green_image
        self.red_e_image = red_e_image

    def get_json(self):
        return {
            "fileName": self.fileName,
            "dt_processed": self.dt_processed,
            "red_image": self.red_image,
            "nir_image": self.nir_image,
            "green_image": self.green_image,
            "red_e_image": self.red_e_image
        }
