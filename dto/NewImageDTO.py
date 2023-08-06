from datetime import datetime


class NewImageDTO:

    def __init__(self,
                 fileName: str,
                 DateTimeProcessed: datetime,
                 red_image,
                 nir_image,
                 green_image,
                 red_e_image,
                 ):
        self.fileName = fileName
        self.DateTimeProcessed = DateTimeProcessed
        self.red_image = red_image
        self.nir_image = nir_image
        self.green_image = green_image
        self.red_e_image = red_e_image
