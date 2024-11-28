import json
import pytest
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

    @pytest.mark.parametrize("endpoint", ["/base/arm_list","/base/product_info","/base/scada_region_list", "/base/server_list", "/health"])
    def test_get_lists_returns_200(self, endpoint, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_with_token(endpoint, access_token)
        
        assert response.status_code == 200
