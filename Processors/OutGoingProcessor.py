import json
from Modules.Messaging.NewImageSender import NewImageSender
from dto.NewImageDTO import NewImageDTO
from dto.CreateSessionRequest import CreateSessionRequest
from dto.CreateImageRequest import CreateImageRequest
import logging
from Modules.ImageReader import ImageReader
from Helpers.NumpyEncoder import NumpyEncoder
import requests
import os


class OutGoingProcessor():

    def __init__(self) -> None:
        self.__init_logger__()
        self.new_image_publisher = NewImageSender()
        self.session_id = ""
        self.headers = {'Content-type': 'application/json'}
        self.new_image_url = f"{os.getenv('API_BASE')}{os.getenv('NEW_IMAGE_ENDPOINT')}"
        self.__register_new_session__()
        self.start()

    def __init_logger__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

    def __callback__(self, image_dto: NewImageDTO):
        self.logger.info(f"Publishing new image: {image_dto.fileName}")

        create_image_request = CreateImageRequest(
            image_dto.fileName, self.session_id, image_dto.path).toJSON()
        response = requests.post(
            self.new_image_url, create_image_request, headers=self.headers)
        if (response.status_code == 200):
            image_dto.id = response.text
            image_dto.session_id = self.session_id
            json_dto = image_dto.get_json()
            json_dto: str = json.dumps(json_dto, cls=NumpyEncoder)
            self.new_image_publisher.publish_new_image(json_dto)
        else:
            raise Exception("Unable to register image")

    def start(self):
        self.image_reader = ImageReader(self.__callback__)
        self.image_reader.start()

    def __register_new_session__(self):
        self.logger.info(
            f"Registering session with name: {os.getenv('SESSION_NAME')}")
        session_request = CreateSessionRequest(
            os.getenv("SESSION_NAME")).toJSON()

        url = f"{os.getenv('API_BASE')}{os.getenv('NEW_SESSION_ENDPOINT')}"

        response = requests.post(url, session_request, headers=self.headers)
        if response.status_code == 200:
            self.session_id = response.text.replace('"', '')
            self.logger.info(f"Session id: {self.session_id}")
        else:
            raise Exception("Unable to register session")
