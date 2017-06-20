from Container import GROUP_CONTAINER
from add_small_funk import value_or_def, join_roles
import Data

class Wrapper:
    """
    Here are all function for work with GroupData and send result to Proxy
    user_roles send form Proxy class
    """
    # default settings
    # add create group method

    def __init__(self, group_key=None, user_roles=None, groups_container=None):
        """

        :param group_key:
        :param user_roles: unregistered may have role == _unregistered
        :param groups_container:
        """
        assert not (user_roles is None), 'User do not have any permission to watch this group'
        self.group_key = group_key
        self.group_data = value_or_def(groups_container, GROUP_CONTAINER).get(self.group_key)
        self.user_roles = user_roles


    def create_group(self, group_name, creator_id, default_permission, default_stat, groups_container=None):
        self.group_key = creator_id + group_name
        group = Data.GroupData(self.group_key)
        setattr(group, 'permission', default_permission)
        setattr(group, 'stat', default_stat)
        self.group_data = value_or_def(groups_container, GROUP_CONTAINER).put(group, self.group_key)

        return self.group_key





    def get_permission(self):
        print '-', self.group_data, GROUP_CONTAINER.container, self.group_key, self.group_data.permission
        return join_roles(self.group_data.permission, self.user_roles)


    def get_stats(self):
        pass

