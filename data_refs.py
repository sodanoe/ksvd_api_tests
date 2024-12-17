class RefSchemas:

    GET_ARM_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": "tester::\u0410\u0420\u041c",
                "descr": r"^.*$",
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
                "descr": r"^.*$",
                "ip": r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
                "port": r"^\d*$",
                "status": r"^\d*$",
                "status_timestamp": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$",
            }
        ]
    }

    GET_PRODUCT_INFO_REF = {
        "product_vendor": r"^.*$",
        "product_name": r"^.*$",
        "product_version": r"^.*$",
    }

    GET_SCADA_REG_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": r"^.*$",
                "descr": r"^.*$",
                "location_x": r"^\d*$",
                "location_y": r"^\d*$",
                "geo_addr": r"^.*$",
            }
        ]
    }

    GET_SERVER_LIST_REF = {
        "list": [
            {
                "id": r"^\d*$",
                "guid": r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}",
                "name": r"^.*$",
                "descr": r"^.*$",
                "status": r"^.*$",
                "status_timestamp": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$",
            }
        ]
    }

    GET_HEALTH_REF = {"status": r"^.*$", "timestamp": r"^\d*$"}
