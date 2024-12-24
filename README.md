# ksvd_api_tests

##     tests/test_ksvd_apis:

        test_login_returns_201(self, http_client):

        test_get_lists_returns_200(self, endpoint, http_client):

        test_compare_json_schemas_wo_guid(self, endpoint, ref, http_client):

        test_get_region_lists_w_guid_returns_200(self, endpoint, ref, http_client):

        test_get_object_lists_w_guid_returns_200(self, endpoint, ref, http_client):

##    data_refs:
        Реферсные значения ответов с регулярными выражениями

##    src/http_client:
        Класс для хттп запросов с логгером для удобства
##   src/ksvd_api:
        login(self):
            Получение токена авторизации

        get_with_token(self, endpoint, access_token)
            Запросы, где требуется acceess-token

        get_region_guid(self, access_token):
            Запросы гуида региона

        get_object_guid(self, access_token):
            Запросы гуида объекта
## utilities:
        JsonCompare.compare(self, reference_json, response_json):
            Сравнение джсона с вложенностью при помощи регулярных выражений