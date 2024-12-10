import re

def test_guid_valid():
    valid_guid = "{dcabda92-c90e-4359-b33d-4ed465a31b26}"
    match_result = re.match(r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}", valid_guid)

    assert match_result is not None, f"{valid_guid} does not match the expected format"
    assert match_result.group(0) == valid_guid, "Mismatch in matched GUID string"

def test_ipv4_address_valid():
    regex = r'\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b'
    valid_ip = "192.168.0.1"
    match = re.match(regex, valid_ip)

    assert match is not None, f"{valid_ip} is not a valid IPv4 address"
