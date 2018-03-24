from parser import *

VERSION = "0.1"

# todo read from command line
VERBOSE_TOKENISER = False
VERBOSE_PARSER = False

def runRepl():
    print "LukeLisp " + VERSION
    while(True):
        program = raw_input("LukeLisp: ")
        parse(program, (VERBOSE_TOKENISER, VERBOSE_PARSER))
        


runRepl()        
