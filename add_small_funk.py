


def value_or_def(obj, default):
    if obj is not None:
        return obj
    else:
        return default

def join_roles(permission={}, roles=[]):
    """"
        if we have same stats with differnt permision
        join roles in next order:
        none -> visible -> change -> hide == 0,1,2,3
        if user hide his stat nobody can change it,
        and we should just return maximum for each stat
    """
    number_of_stats = len(permission[roles[0]])
    zip_permision = []
    for i in range(number_of_stats):
        zip_permision.append(0)
        for role in roles:
            if permission[role][i] > zip_permision[i]:
                zip_permision[i] = permission[role][i]
    return zip_permision



if __name__ == '__main__':
    """ TEST """
    permission = ({
    # role [none=0, visible=1, change=2, hide=3, ]
    "admin": [0,1],
    "user": [0,1],
    "_creator": [2,0],  # creator can add users
    "_own": [0,2],  # change or visible only own stats
    "_unregistered": [0,0]  # for user without aouth
    })
    print "role: user and _creator: ", join_roles(permission, ['user', '_creator'])
