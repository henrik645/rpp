class Assignment:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def eval(self, env):
        env[self.left.id] = self.right.eval(env)
        
    def __repr__(self):
        return "Assignment: {0} = {1}".format(self.left, self.right)
