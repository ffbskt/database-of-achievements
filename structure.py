OTG_CONTAINER = {}
GROUP_CONTEINER = {}

class OTGData:
    def __init__(self, key):
        self.key = key
        self.roles__ = []


class GroupData:
    def __init__(self):
        self.stats = []
        self.roles = {}
        self.name = ''


class UserAouth:
    def __init__(self, user_key):
        self.UserKey = user_key
        if user_key is None:
            self.UserKey = raw_input('key ')

    def check_permision(self):
        pass

    def get_user(self):
        return self.UserKey


class AbstractCreator(object): # ?no need
    def __init__(self):
        pass


class OTGCreator(AbstractCreator): # maybe fogot
    def __init__(self):
        super(self.__class__, self).__init__()

    # create - ???



class GroupCreator(AbstractCreator):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create(self, user_key, group_name):
        key = user_key + group_name

        group = GroupData()
        group.name = group_name
        GROUP_CONTEINER[key] = group
        otg = OTGData(key=group_name + user_key)
        otg.roles__.append('__creator')
        OTG_CONTAINER[otg.key] = otg
        return GROUP_CONTEINER[key]


class ShowAll:
    pass


class GroupWrapper(object):
    def __init__(self, group, default_role="user"):
        self.group = group
        self.default_role = default_role

    def get_self_stat(self):
        pass

    def get_link_stat(self):
        pass

    def permision(self, user):
        if hasattr(user, 'roles__'):
            return self.group.roles[user.roles__[0]]

        return None

    def edit(self, message):
        self.group.stats.extend(message['stats'])
        self.group.roles.update(message['roles'])


class OTGProxy: # for all objects(OTG) servise..
    def __init__(self, user_key):  # ?user_key or multiple users []
        self.user_key = user_key

    def put_object_to_group(self, obj, groupwraper):
        self.groupwrapper = groupwraper
        otg_key = groupwraper.group.name + user_key
        user = OTG_CONTAINER[otg_key]
        print user.roles__
        permision = groupwraper.permision(user=user)
        print '--', permision
        assert not (permision is None or not ('@invite' in permision)), "No permision"
        self.otg = OTGData(key=obj + groupwraper.group.name)
        self.otg.roles__ = groupwraper.default_role
        self.create(VisitorHistory())
        OTG_CONTAINER[self.otg.key] = self.otg
        print "OK entity put"
        #is user can add -> group
        pass

    def edit(self):
        pass

    def show(self):
        pass

    def create(self, visitor):
        for st in self.groupwrapper.group.stats:
            visitor.create(self.otg, st, 988)#setattr(self.otg, st, 0)

    def compute(self):
        pass

class VisitorHistory:
    def __init__(self):
        pass

    def create(self, otg, st, val):
        setattr(otg, st, val)

    def show(self):
        pass


""""
class BackEndFunctionSimulator:
    def put_object_to_group(self, obj, group):
        user = UserAouth('A').get_user()
        gw = GroupWrapper(group)
        gw.permision(user, obj)

        print 'BS ptg'

"""


if __name__ == "__main__":

    user_key = UserAouth('A').get_user()
    print user_key
    c = GroupCreator() #+ autor by Auth
    g = c.create(user_key, 'g1')
    #print hasattr(g, "roles")

    w = GroupWrapper(g, default_role='staff') # + user Aouth
    w.edit({'stats': ['money', 'prise'], 'roles': {'user': 'money', 'staff': 'prise', '__creator': '@invite'}})
    print GROUP_CONTEINER, GROUP_CONTEINER['Ag1'].roles, OTG_CONTAINER['g1A'].roles__

    #obj = OTGData(key='shoes')

    p_otg = OTGProxy(user_key)  # Object To Group
    p_otg.put_object_to_group(obj='shoes', groupwraper=w)
    p_otg.put_object_to_group(obj='string', groupwraper=w)
    #bs.put_object_to_group(user)
    print OTG_CONTAINER
    print OTG_CONTAINER['shoesg1'].prise

    #create stats to OTG
