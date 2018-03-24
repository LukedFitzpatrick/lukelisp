import re

# turn a program string into a list of tokens
def tokenise(program):
    # todo learn regex properly and make this a one liner
    program = re.sub("\(", " ( ", program)
    program = re.sub("\)", " ) ", program)
    
    return program.split()


def tokenToAtom(token):
    # Int atom
    try:
        return int(token)
    except ValueError:
        pass

    # float atom
    try :
        return float(token)
    except ValueError:
        pass

    # todo add string/list atom?
    
    # variable/function name (symbol) atom
    return str(token)
        

def tokensToTree(tokens):
    if(len(tokens) == 0):
        raise SyntaxError("tokensToTree: Reached end of input unexpectedly")

    token = tokens.pop(0)

    # start a new expression which consists of a number of expressions
    if(token == "("):
        exprs = []
        while tokens[0] != ")":
            exprs.append(tokensToTree(tokens))

        # consume the )
        tokens.pop(0)
        return exprs

    # we shouldn't be ending the expr here, this is a bad expression
    elif(token == ")"):
        raise SyntaxError("tokensToTree: Unexpected ) at start of expression")

    # just an atomic expression e.g. an Int or a variable name
    else:
        return tokenToAtom(token)

# given a program string, returns an AST
def parse(program, verbosity):
    (VERBOSE_TOKENISER, VERBOSE_PARSER) = verbosity
    
    tokens = tokenise(program)
    if VERBOSE_TOKENISER: print tokens

    tree = tokensToTree(tokens)
    if VERBOSE_PARSER: print tree

    return tree
