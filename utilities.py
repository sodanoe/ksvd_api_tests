from logging import getLogger
import re

logger = getLogger(__name__)


class JsonCompare:

    def compare(self, reference_json, response_json):
        state = True
        for key in reference_json.keys():
            if isinstance(reference_json[key], dict):
                state = self.compare(reference_json[key], response_json[key])
            elif isinstance(reference_json[key], list):
                for i, item in enumerate(response_json[key]):
                    state = self.compare(reference_json[key][0], response_json[key][i])
            else:

                regex = reference_json[key]
                value = str(response_json[key])

                if not re.match(regex, value):
                    logger.error(f"'{value}' does not match '{regex}'.")
                    state = False

            if key not in response_json:
                logger.error(f"Key {key} not found.")
                state = False
        return state


print(re.match(r'^[^\s.]*[^\s.]\s*[^\s.]*[^\s.]*$', ''))