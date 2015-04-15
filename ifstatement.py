class IfStatement:
    def __init__(self, condition, if_body, else_body=None):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body
        
    def eval(self, env):
        if self.condition.eval(env):
            self.if_body.eval(env)
        elif self.else_body is not None:
            if not self.condition.eval(env):
                self.else_body.eval(env)
            
    def __repr__(self):
        return "IfStatement: {0} {1}".format(self.condition, self.body)
