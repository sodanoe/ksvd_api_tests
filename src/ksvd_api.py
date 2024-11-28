from src.http_client import HttpClient, HttpMethods


class KsvdApi:

    def __init__(self, client: HttpClient):
        self.client = client


    def login(self):
        body = {"password": "admin", "username": "admin"}
        response = self.client.send_request(HttpMethods.POST, "/login", json=body)
        return response
    