import json


class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
