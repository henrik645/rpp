class Binop:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
        
    def eval(self, env):
        lval = self.left.eval(env)
        rval = self.right.eval(env)
        if self.op == "+":
            val = lval + rval
        elif self.op == "-":
            val = lval - rval
        elif self.op == "*":
            val = lval * rval
        elif self.op == "/":
            val = lval / rval
        return val
        
    def __repr__(self):
        return "Binop: {0} {1} {2}".format(self.left, self.op, self.right)
