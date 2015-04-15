class Identifier:
    def __init__(self, id):
        self.id = id
        
    def eval(self, env):
        if self.id in env:
            return env[self.id]
        else:
            error("Referencing " + self.id + " before assignment")
        
    def __repr__(self):
        return "Identifier: {0}".format(self.id)
