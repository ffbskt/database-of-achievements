


class Visitor(object):
    def show(self):
        pass

    def edit(self):
        pass


class SimpleData(Visitor):
    pass


class RoleDictionary(Visitor):
    def edit(self):
        pass

class Dict(Visitor):
    def edit(self, dictionary):
        return dictionary



class StatOpt(Visitor):
    def edit(self):
        pass
