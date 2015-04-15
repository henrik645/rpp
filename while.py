class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
        
    def eval(self, env):
        while self.condition.eval(env):
            self.body.eval(env)
            
    def __repr__(self):
        return "While: {0} {1}".format(self.condition, self.body)
