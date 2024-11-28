import json
from src.ksvd_api import KsvdApi

class TestKsvd:

    access_token = ""

    def test_login_returns_201(self, http_client):
        global access_token
        
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.login()
        ans = json.loads(response.text)
        access_token = ans["data"]["access_token"]

        assert response.status_code == 201

    def test_arm_list_returns_200(self, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_arm_list(access_token)
        
        assert response.status_code == 200
