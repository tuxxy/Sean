import json

from .seantype import SeanType
from .handlers import DEFAULT_HANDLERS


class Sean(object):
    def __init__(self, sean_formatted_json, override_handlers={}):
        self.sean_json = json.loads(sean_formatted_json)
        self.handlers = DEFAULT_HANDLERS
        self.handlers.update(override_handlers)
        self.sean_types = self._expand_json(self.sean_json)

    def seanify(self, format_json=False):
        data = self._exec_types()
        if format_json:
            data = json.dumps(data)
        return data

    def _expand_json(self, sean_data):
        data = {}
        # Because of this, there can't be any child lists.
        # This probably needs a rewrite to handle all of these recursive cases
        # Might be able to be solved with a caller method that iterates over the
        # top-most dict and every received dict is treated differently.
        sean_data = (sean_data.get('_val', None) or sean_data)
        for key, value in sean_data.items():
            if isinstance(value, dict):
                _type = value.get('_type', None)
                if _type == 'dict':
                    data[key] = self._expand_json(value['_val'])
                elif _type == 'list':
                    data_list = []
                    for i in range(0, value.get('_len', 1)):
                        data_list.append(self._expand_json(value['_val']))
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
                        data_list.append(self._expand_json(val))
                    data[key] = data_list
        return data

    def _exec_types(self, sean_data=None):
        if sean_data != None:
            sean_types = sean_data
        else:
            sean_types = self.sean_types

        if isinstance(sean_types, dict):
            data = {}
            for key, value in sean_types.items():
                if isinstance(value, SeanType):
                    data[key] = value.exec_handler()
                elif isinstance(value, dict):
                    data[key] = self._exec_types(sean_data=value)
                elif isinstance(value, list):
                    data_list = []
                    for val in value:
                        data_list.append(self._exec_types(sean_data=val))
                    data[key] = data_list
        elif isinstance(sean_types, list):
            data = []
            for idx, value in enumerate(sean_types):
                if isinstance(value, SeanType):
                    data[idx] = value.exec_handler()
                elif isinstance(value, dict):
                    data[idx] = self._exec_types(sean_data=value)
                elif isinstance(value, list):
                    data_list = []
                    for val in value:
                        data_list.append(self.exec_types(sean_data=val))
                    data[idx] = data_list
        return data
