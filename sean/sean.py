import json
import string
import random
import warnings

from faker import Faker

from seantype import SeanType
from handlers import DEFAULT_HANDLERS


class Sean(object):
    def __init__(self, sean_formatted_json, override_handlers={}):
        self.sean_json = json.loads(sean_formatted_json)
        self.handlers = DEFAULT_HANDLERS
        self.handlers.update(override_handlers)
        self.sean_types = self.seanify(sean_json=self.sean_json)
        
    def seanify(self, sean_json=None):
        sean_data = (sean_json or self.sean_types)
        data = self._handle_data(sean_data)
        return data

    def _handle_data(self, sean_data):
        data = {}
        for key, value in sean_data.items():
            if isinstance(value, SeanType):
                data[key] = value.exec_handler()
            elif isinstance(value, dict):
                _type = value.get('_type', None)
                if _type == 'dict':
                    data[key] = self._handle_data(value['_val'])
                elif _type == 'list':
                    data_list = []
                    for i in range(0, value.get('_len', 1)):
                        data_list.append(self._handle_data(value['_val']))
                    data[key] = data_list
                elif _type:
                    data[key] = SeanType(self.handlers[_type], **value)
            elif isinstance(value, list):
                # This prevents a Sean 'list' from being overwritten.
                if not isinstance(value[0], dict):
                    data[key] = SeanType(self.handlers[None], _val=value)
                else:
                    data_list = []
                    for idx, val in enumerate(value):
                        data_list.append(self._handle_data(val))
                    data[key] = data_list
        return data
