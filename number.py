class Number:
    def __init__(self, value):
        self.value = value
        
    def eval(self, env):
        return self.value
        
    def __repr__(self):
        return "Number: {0}".format(self.value)
