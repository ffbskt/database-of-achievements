


class Data(object):
    def __init__(self, key):
        self.key = key


class GroupData(Data):
    def __init__(self, key):
        super(self.__class__, self).__init__(key=key)
        self.permission = {}
        self.stats = []


class ObjectData(Data):
    def __init__(self, key):
        super(self.__class__, self).__init__(key=key)
        self._roles = []
