import json


class CreateImageRequest():
    def __init__(self, filename, session_id, filePath) -> None:
        self.fileName = filename
        self.sessionId = session_id
        self.filePath = filePath

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
