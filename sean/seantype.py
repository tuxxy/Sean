class SeanType(object):
    def __init__(self, **kwargs):
        # A SeanType always has a type and a value, even None.
        self._type = kwargs.get('_type', None)

        self.params = kwargs
