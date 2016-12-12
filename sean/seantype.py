class SeanType(object):
    def __init__(self, handler_func, **kwargs):
        self.handler_func = handler_func

        self._type = kwargs.get('_type', None)
        self.params = kwargs

    def exec_handler(self):
        return self.handler_func(**self.params)
