import json


class CreateSessionRequest():
    def __init__(self, name: str) -> None:
        self.SessionName = name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
