from Wrapper import Wrapper
import Container
from Visitors import *
from add_small_funk import *

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
        wrap = Wrapper(user_role=self.get_user_role())
        wrap.get_permission()

        pass

    def show_group_stat(self):
        pass

    def create_group(self, name):
        wrap = Wrapper(group_key=self.group_key, user_roles=self.user_role)
        self.group_key = wrap.create_group(name, self.user_id)

    def get_user_role(self):
        self.user_key = self.user_id + self.group_key
        try:
            return self.users_container[self.user_key].__role
        except AttributeError:
            raise Exception('You are not here')




