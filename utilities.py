from logging import getLogger

logger = getLogger(__name__)


class JsonCompare:
    def __init__(self, reference_json, response_json):
        self.reference_json = reference_json
        self.response_json = response_json

    def compare(self):
        for key in self.reference_json.keys():
            if key == "list":
                ref_list = self.reference_json[key][0]
                resp_list = self.response_json[key][0]
                for ref_key in ref_list:
                    if ref_key not in resp_list:
                        logger.error(f'Key {ref_key} not in {resp_list}.')
                        return False 
            if key not in self.response_json:
                logger.error(f'Key {key} not found.')
                return False
        return True
