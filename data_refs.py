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

    GET_REGION_LIST = {
        "list": [
            {
                "id": 1,
                "guid": "{1b21b2ad-e98a-46a7-8f23-922157daac78}",
                "name": "region",
                "descr": "",
                "location_x": 0,
                "location_y": 0,
                "geo_addr": "",
            }
        ]
    }

    GET_OBJECT_LIST = {
        "list": [
            {
                "id": 3,
                "guid": "{6c4ec5a1-f811-472e-9725-a2fd57d05103}",
                "name": "Камера",
                "descr": "",
                "location_x": 0,
                "location_y": 0,
                "geo_addr": "",
                "addr": "",
                "phone": "",
            }
        ]
    }

    GET_CAMERAS_LIST = {
        "list": [
            {
                "id": 5,
                "guid": "{e62d343d-8cca-4865-ad95-42037f9ac906}",
                "name": "Камера 1",
                "descr": "",
                "stream": "",
                "status": 0,
                "status_timestamp": "",
                "status_color": "",
                "location_x": 0,
                "location_y": 0,
                "direction": 0,
            },
        ]
    }

    GET_LAYOUT_LIST = {
        "list": [
            {
                "id": 5,
                "guid": "{46de5e87-79b8-47fd-a5f8-2229f67265ef}",
                "name": "Камера 1",
                "descr": "",
                "monitors": [
                    {
                        "num": 1,
                        "name": "Монитор 01",
                        "descr": "auto",
                        "grid_width": 1,
                        "grid_height": 2,
                        "cameras": [
                            {
                                "x1": 0,
                                "y1": 0,
                                "x2": 0,
                                "y2": 0,
                                "camera_guid": "{e62d343d-8cca-4865-ad95-42037f9ac906}",
                                "camera_stream": [],
                            }
                        ],
                    }
                ],
            },
            {
                "id": 6,
                "guid": "{485bffb1-ac65-4bea-b653-468282446f73}",
                "name": "Камера 2",
                "descr": "",
                "monitors": [
                    {
                        "num": 1,
                        "name": "Монитор 01",
                        "descr": "auto",
                        "grid_width": 1,
                        "grid_height": 2,
                        "cameras": "null",
                    }
                ],
            },
            {
                "id": 7,
                "guid": "{c4f9a8ad-8996-42d9-ba47-bc0e89ecf760}",
                "name": "Камера 3",
                "descr": "",
                "monitors": [
                    {
                        "num": 1,
                        "name": "Монитор 01",
                        "descr": "auto",
                        "grid_width": 1,
                        "grid_height": 2,
                        "cameras": "null",
                    }
                ],
            },
        ]
    }
