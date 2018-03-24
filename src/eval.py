# evaluate an expression with a given environment
# todo error checking/messages
def evaluate(ast, env):

    # ints/floats eval to themselves
    if isinstance(ast, int) or isinstance(ast, float):
        return ast

    # if we see just a raw symbol, look it up in the env
    elif isinstance(ast, str):
        if not ast in env:
            raise SyntaxError("evaluate: %s is undefined" % ast)
        else:
            return env[ast]

    # must be a list
    # special form: if
    elif (ast[0] == "if"):
        test = evaluate(ast[1], env)
        if(test):
            return evaluate(ast[2], env)
        else:
            return evaluate(ast[3], env)

    # special form: define
    elif (ast[0] == "def"):
        value = evaluate(ast[2], env)
        env[ast[1]] = value

        return str(ast[1]) + "=" + str(value)
        
    # any other list is a procedure call
    else:
        func = evaluate(ast[0], env)
        args = []
        for arg in ast[1:]:
            args.append(evaluate(arg, env))

        return func(*args)
