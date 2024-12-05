import json

from src.http_client import HttpClient, HttpMethods


class KsvdApi:

    def __init__(self, client: HttpClient):
        self.client = client

    def login(self):
        body = {"password": "admin", "username": "admin"}
        response = self.client.send_request(HttpMethods.POST, "/login", json=body)

        return response

    def get_with_token(self, endpoint, access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.client.send_request(
            HttpMethods.GET, endpoint=endpoint, headers=headers
        )

        return response
