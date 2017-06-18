import Auth, Proxy
import Container

id = Auth.Auth().get_user_id()
proxy = Proxy.Proxy(id)
permission = ({
		"admin":{"change":[],
			"visible":[], "hide":[]},
		"user":{"change":["@name"], # @ - Only own
		    	"visible":[], "hide":[]},
		"__creator":{"change":['@invite'],
			   "visible":[], "hide":[]},
		"__id":{"change":['@invite'],
			   "visible":[], "hide":[]}
		 })
stat_opt = ({'st_name':[], 'default':[], 'opt':[]})
proxy.create_group('Group1')

proxy.edit_group_stat(stat_name='permission', stat_value=permission, stat_opt='Dict')

print Container.GROUP_CONTAINER.container
#proxy.edit_group_stat(permission, stat_opt, name)
