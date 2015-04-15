class Statements:
    def __init__(self, statements):
        self.statements = statements
    
    def eval(self, env):
        for statement in self.statements:
            statement.eval(env)
            
    def __repr__(self):
        string = "Statements:"
        for statement in self.statements:
            string += "\n{0}".format(statement)
        string += "\n-END-\n"
        return string
