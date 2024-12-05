import json
import pytest


from data_refs import RefSchemas
from utilities import JsonCompare
from src.ksvd_api import KsvdApi
from logging import getLogger

logger = getLogger(__name__)


class TestKsvd:

    access_token = ""

    def test_login_returns_201(self, http_client):
        global access_token

        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.login()
        ans = json.loads(response.text)
        try:
            access_token = ans["data"]["access_token"]
        except TypeError as e:
            logger.error(f'Can not get access_token. Error: {e}')

        assert response.status_code == 201

    @pytest.mark.parametrize("endpoint", ["/base/arm_list","/base/product_info","/base/scada_region_list", "/base/server_list", "/health"])
    def test_get_lists_returns_200(self, endpoint, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_with_token(endpoint, access_token)

        assert response.status_code == 200

    @pytest.mark.parametrize("endpoint, ref", [
        ("/base/arm_list", RefSchemas.GET_ARM_LIST_REF),
        ("/base/product_info", RefSchemas.GET_PRODUCT_INFO_REF),
        ("/base/scada_region_list", RefSchemas.GET_SCADA_REG_LIST_REF), 
        ("/base/server_list", RefSchemas.GET_SERVER_LIST_REF), 
        ("/health", RefSchemas.GET_HEALTH_REF)])
    def test_compare_product_info_ret_true(self, endpoint, ref, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_with_token(endpoint, access_token)
        response_json = response.json()
        compare = JsonCompare(ref, response_json["data"])

        assert compare.compare()
