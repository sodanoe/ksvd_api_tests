from src.ksvd_api import KsvdApi

class TestKsvd:

    def test_login_returns_201(self, http_client):
        ksvd_api = KsvdApi(http_client)
        resoponse = ksvd_api.login()
        assert resoponse.status_code == 201
