from src.http_client import HttpClient, HttpMethods


class KsvdApi:

    def __init__(self, client: HttpClient):
        self.http_client = client
