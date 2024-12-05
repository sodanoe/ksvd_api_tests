from logging import getLogger

logger = getLogger(__name__)


class JsonCompare:

    def compare(self, reference_json, response_json):
        for key in reference_json.keys():
            if key == "list":
                return self.compare(reference_json[key][0], response_json[key][0])
            if key not in response_json:
                logger.error(f"Key {key} not found.")
                return False
        return True
