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

    def get_region_guid(self, access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.client.send_request(
            HttpMethods.GET, endpoint="/base/scada_region_list", headers=headers
        )
        response_json = response.json()
        guid = response_json["data"]["list"][0]["guid"]

        return guid

    def get_object_guid(self, access_token):
        region_guid = self.get_region_guid(access_token)
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.client.send_request(
            HttpMethods.GET,
            endpoint=f"/base/scada_object_list/{region_guid}",
            headers=headers,
        )
        response_json = response.json()
        guid = response_json["data"]["list"][0]["guid"]

        return guid
