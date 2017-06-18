from Container import GROUP_CONTAINER
from add_small_funk import value_or_def

class Wrapper:

    # default settings
    # add create group method

    def __init__(self, group_key=None, user_roles=None, groups_container=None):
        self.group_key = group_key
        self.group_data = value_or_def(groups_container, GROUP_CONTAINER).get(self.group_key)
        self.user_roles = user_roles


    def create_group(self, group_name, creator_id, groups_container=None):
        self.group_key = creator_id + group_name
        self.group_data = value_or_def(groups_container, GROUP_CONTAINER).get(self.group_key)

        return self.group_key





    def get_permission(self):
        return self.group_data.permission[self.user_role]

    def get_stats(self):
        pass

