import re

class SymbolToken:
    def __init__(self, val):
        self.value = val

# turn a program string into a list of tokens
def tokenise(program):
    tokens = []
    thisToken = ""
    inQuote = False
    
    while(len(program) > 0):
        thisChar = program[0]
        program = program[1:]

        if(thisChar == '"'):
            if inQuote:
                thisToken += thisChar
                if(len(thisToken) > 0):
                    tokens.append(thisToken)
                thisToken = ""
                inQuote = False
            else:
                if(len(thisToken) > 0):
                    tokens.append(thisToken)
                thisToken = thisChar
                inQuote = True
                
            
        elif(thisChar in (" ", "(", ")") and not inQuote):
            if(len(thisToken) > 0):
                tokens.append(thisToken)
                thisToken = ""
            if(thisChar != " "):
                tokens.append(thisChar)
                
        else:
            thisToken += thisChar

    return tokens

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

    if(len(token) > 1):
        if(token[0] == '"' and token[-1] == '"'):
            return str(token[1:-1])
    
    # variable/function name (symbol) atom
    return SymbolToken(token)

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
