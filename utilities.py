from logging import getLogger

logger = getLogger(__name__)


class JsonCompare:
    def __init__(self, reference_json, response_json):
        self.reference_json = reference_json
        self.response_json = response_json

    def compare(self):
        for key in self.reference_json.keys():
            if key not in self.response_json:
                logger.error(f'Key {key} not found.')
                return False
        return True
