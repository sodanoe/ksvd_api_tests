class RefSchemas:

    GET_ARM_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": "tester::\u0410\u0420\u041c",
                "descr": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "ip": r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
                "port": r"^\d*$",
                "status": r"^\d*$",
                "status_timestamp": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$",
            }
        ]
    }

    GET_ARM_LIST_REGEX = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": "tester::\u0410\u0420\u041c",
                "descr": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "ip": r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
                "port": r"^\d*$",
                "status": r"^\d*$",
                "status_timestamp": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$",
            }
        ]
    }

    GET_PRODUCT_INFO_REF = {
        "product_vendor": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
        "product_name": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
        "product_version": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
    }

    GET_SCADA_REG_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "descr": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "location_x": r"^\d*$",
                "location_y": r"^\d*$",
                "geo_addr": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
            }
        ]
    }

    GET_SERVER_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "descr": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "status": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$',
                "status_timestamp": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$",
            }
        ]
    }

    GET_HEALTH_REF = {"status": r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$', "timestamp": r"^\d*$"}
