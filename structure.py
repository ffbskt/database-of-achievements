OTG_CONTAINER = {}
GROUP_CONTEINER = {}

class OTGData:
    pass

class GroupWrapper(object):
    def __init__(self, group):
        self.group = group

    def get_self_stat(self):
        pass

    def get_link_stat(self):
        pass

    def permision(self):
        pass

    def edit(self, message):
        self.group.stats.extend(message['stats'])
        self.group.roles.update(message['roles'])


class GroupData:
    def __init__(self):
        self.stats = []
        self.roles = {}


class UserAouth:
    def __init__(self, user_key):
        self.UserKey = user_key
        if user_key is None:
            self.UserKey = raw_input('key ')
        if self.UserKey in OTG_CONTAINER:
            print 'signIn'
        else:
            #Create OTG
            OTG_CONTAINER[self.UserKey] = OTGData()
        print OTG_CONTAINER

    def check_permision(self):
        pass

    def get_user(self):
                return OTG_CONTAINER[self.UserKey]

class AbstractCreator(object):
    def __init__(self):
        pass


class OTGCreator(AbstractCreator):
    def __init__(self):
        super(self.__class__, self).__init__()

    # create - ???



class GroupCreator(AbstractCreator):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create(self, key):
        GROUP_CONTEINER[key] = GroupData()
        return GROUP_CONTEINER[key]


class ShowAll:
    pass


class OTGProxy:
    def __init__(self, current_object):
        self.current_object = current_object

    def add(self, group):
        #is user can add -> group
        pass

    def edit(self):
        pass

    def show(self):
        pass

    def create(self):
        pass

    def compute(self):
        pass


if __name__ == "__main__":
    user = UserAouth('A').get_user()
    print user
    c = GroupCreator() #+ autor by Auth
    g = c.create('g1')
    w = GroupWrapper(g) # + user Aouth
    w.edit({'stats': ['a', 'b'], 'roles': {'A': 'a', 'B': 'b'}})
    print GROUP_CONTEINER, GROUP_CONTEINER['g1'].roles

    p_otg = OTGProxy(user)
    p_otg.edit()


    #create stats to OTG
