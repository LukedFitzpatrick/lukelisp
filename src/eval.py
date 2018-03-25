from parser import SymbolToken

class PrintVal:
    def __init__(self, val):
        self.value = val

# evaluate an expression with a given environment
# todo error checking/messages
# returns value, print flag (whether we need to print the result)
def evaluate(ast, env):
    if isinstance(ast, SymbolToken):
        if not ast.value in env:
            raise SyntaxError("evaluate: %s is undefined" % ast.value)
        else:
            return env[ast.value]

    # basic types eval to themselves
    elif isinstance(ast, int) or isinstance(ast, float) or isinstance(ast, str):
        return ast

    # must be a list    
    elif isinstance(ast[0], SymbolToken):
        # special form: if
        if (ast[0].value  == "if"):
            test = evaluate(ast[1], env)
            if(test):
                return evaluate(ast[2], env)
            else:
                return evaluate(ast[3], env)

        # special form: set
        elif (ast[0].value  == "set"):
            value = evaluate(ast[2], env)
            if(isinstance(ast[1], SymbolToken)):
               env[ast[1].value] = value
               return str(ast[1]) + "=" + str(value)
            else:
               raise SyntaxError("Tried to assign to a non-symbol") 

        # special form: print
        elif (ast[0].value  == "print"):
            result = evaluate(ast[1], env)
            if(isinstance(result, SymbolToken)):
               return PrintVal(result.value)
            else:
               return PrintVal(result)

        # maybe a function in the env
        else:
            func = evaluate(ast[0], env)
            args = []
            for arg in ast[1:]:
                args.append(evaluate(arg, env))

            return func(*args)

    else:
        raise SyntaxError("Unhandled case in parser:" + str(ast))
