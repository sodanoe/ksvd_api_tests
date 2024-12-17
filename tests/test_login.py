import json
import pytest

from data_refs import RefSchemas
from utilities import JsonCompare
from src.ksvd_api import KsvdApi
from logging import getLogger

logger = getLogger(__name__)

EP = [
    "/base/arm_list",
    "/base/product_info",
    "/base/scada_region_list",
    "/base/server_list",
    "/health",
]

EP_AND_REFS = [
    ("/base/arm_list", RefSchemas.GET_ARM_LIST_REF),
    ("/base/product_info", RefSchemas.GET_PRODUCT_INFO_REF),
    ("/base/scada_region_list", RefSchemas.GET_SCADA_REG_LIST_REF),
    ("/base/server_list", RefSchemas.GET_SERVER_LIST_REF),
    ("/health", RefSchemas.GET_HEALTH_REF),
]

EP_W_GUID = [
    "/base/scada_camera_list/{guid}",
    "/base/scada_layout_list/{guid}",
    "/base/scada_object_list/{guid}",
    "/base/scada_object_list/{guid}",
]


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
            logger.error(f"Can not get access_token. Error: {e}")

        assert response.status_code == 201

    @pytest.mark.parametrize("endpoint", EP)
    def test_get_lists_returns_200(self, endpoint, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_with_token(endpoint, access_token)

        assert response.status_code == 200

    @pytest.mark.parametrize("endpoint", EP_W_GUID)
    def test_get_lists_w_guid_returns_200(self, endpoint, http_client):
        ksvd_api = KsvdApi(http_client)
        guid = ksvd_api.get_scada_guid(access_token)
        response = ksvd_api.get_with_token(f"{endpoint}{guid}", access_token)

        assert response.status_code == 200

    @pytest.mark.parametrize("endpoint, ref", EP_AND_REFS)
    def test_compare_json_schemas(self, endpoint, ref, http_client):
        ksvd_api = KsvdApi(http_client)
        response = ksvd_api.get_with_token(endpoint, access_token)
        response_json = response.json()
        compare = JsonCompare()

        assert compare.compare(ref, response_json["data"])
