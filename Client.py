import Auth, Proxy
import Container

id = Auth.Auth().get_user_id()
proxy = Proxy.Proxy(id)

proxy.create_group('Group1')

#permission = {}
#proxy.edit_group_stat(stat_name='permission', stat_value=permission, stat_opt='Dict')

print "Finally of create group we have GroupData with permission to invite new peuple for creator," \
      "We create ObjectData it's user who create a group"
print Container.GROUP_CONTAINER.container, Container.GROUP_CONTAINER.container['123Group1'].permission
print Container.USER_CONTAINER.container, Container.USER_CONTAINER.container['123Group1123']._roles
#proxy.edit_group_stat(permission, stat_opt, name)
