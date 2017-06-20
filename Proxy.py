from Wrapper import Wrapper
import Container
import Data
from Visitors import *
from add_small_funk import *


"""
    In permission:
    "admin": [0,2] mean user admin can't see or change first statistic ('_invite')
                and can change second ('name') in st_name
    if stat = {'st_name':['_invite', 'name']}
"""
DEFAULT_PERMISSION = {
    # role [none=0, visible=1, change=2, hide=3, ]
    "admin": [0],
    "user": [0],
    "_creator": [2],  # creator can add users
    "_own": [0],  # change or visible only own stats
    "_unregistered": [0]  # for user without aouth
    }

DEFAULT_STAT = {'st_name': ['_invite'], 'default': [True], 'opt': ['GroupInviter']}

class Proxy:
    def __init__(self, user_id, users_container=None):
        self.users_container = value_or_def(users_container, Container.USER_CONTAINER)
        self.user_id = str(user_id)
        self.user_key = None # for concrete group (self.user_id + self.group_key)
        self.group_key = None
        self.user_role = None

    def ask_wrapper(self):
        return 0

    def edit_user_stat(self):
        pass

    def show_user_stat(self):
        pass


    def edit_group_stat(self, stat_name, stat_value, stat_opt, group_key=None):
        print self.get_user_role()
        wrap = Wrapper(user_roles=self.get_user_role(), group_key=self.group_key)
        wrap.get_permission()

        pass

    def show_group_stat(self):
        pass

    def create_group(self, name, default_permission=DEFAULT_PERMISSION, default_stat=DEFAULT_STAT):
        self.user_role = 'unknown'  # mistake if we want made group in group
        wrap = Wrapper(group_key=self.group_key, user_roles=self.user_role)
        # add funktion could we made group here
        #if wrap.get_permission()['create']
        self.user_role = '_creator'
        self.group_key = wrap.create_group(name, self.user_id, default_permission, default_stat)
        self.create_object_data(self.user_id, self.group_key, self.user_role)


    def get_user_role(self):
        self.user_key = self.group_key + self.user_id
        try:
            return self.users_container.get(self.user_key)._roles
        except AttributeError:
            raise Exception('You are not here')

    def create_object_data(self, user_id, group_key, role):
        user_key = group_key + user_id
        user = Data.ObjectData(user_key)
        user._roles.append(role)
        self.users_container.put(obj=user, key=user_key)
        #print 'c  ', self.users_container.container

