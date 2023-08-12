from datetime import datetime


class NewImageDTO:

    def __init__(self,
                 fileName: str,
                 dt_processed: datetime,
                 id: str):
        self.id = id
        self.fileName = fileName
        self.dt_processed = dt_processed

    def get_json(self):
        return {
            "id": self.id,
            "fileName": self.fileName,
            "dt_processed": self.dt_processed,
        }
