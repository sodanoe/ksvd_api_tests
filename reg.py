import re
from logging import getLogger

logger = getLogger(__name__)

class RegexpChecks:

    def is_guid_valid(guid):
        logger.info(f"Input is {guid}\n")

        match_result = re.match(r"\{[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\}", guid)

        if match_result is not None:
            return True
        else:
            return False

    def test_ipv4_address_valid():
        regex = r'\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b'
        valid_ip = "192.168.0.1"
        match = re.match(regex, valid_ip)

        assert match is not None, f"{valid_ip} is not a valid IPv4 address"
