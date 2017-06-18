import Data

class Conteiner(object):
    def __init__(self):
        self.container = {}
        self.default_entity = Data.Data()

    def get(self, key):
        if key is None:
            return None
        if key in self.container:
            return self.container[key]
        else:
            self.put(self.default_entity, key)
            return self.default_entity


    def put(self, obj, key):
        if key is None:
            assert "container key is None"
        self.container[key] = obj

class GroupContainer(Conteiner):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.default_entity = Data.GroupData()  # ??

class UserContainer(Conteiner):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.default_entity = Data.UserData()  # ??


GROUP_CONTAINER = Conteiner()
USER_CONTAINER = Conteiner()
