from datetime import datetime
import os


class NewImageDTO:

    def __init__(self,
                 fileName: str,
                 dt_processed: datetime,
                 path: str
                 ):
        self.fileName = fileName
        self.dt_processed = dt_processed
        self.id = ""
        self.path = path
        self.session_id = ""

    def get_json(self):
        return {
            "id": self.id,
            "fileName": self.fileName,
            "dt_processed": self.dt_processed,
            "session_id": self.session_id
        }
