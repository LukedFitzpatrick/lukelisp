from parser import *
from environment import *
from eval import *

VERSION = "0.1"

# todo read from command line
VERBOSE_TOKENISER = False
VERBOSE_PARSER = False

def runRepl():
    env = getStandardEnv()
    
    print "LukeLisp " + VERSION
    while(True):
        program = raw_input("LukeLisp: ")
        ast = parse(program, (VERBOSE_TOKENISER, VERBOSE_PARSER))
        print evaluate(ast, env)
        
runRepl()        
