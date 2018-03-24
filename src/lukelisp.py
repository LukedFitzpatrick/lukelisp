from parser import *
from environment import *
from eval import *
import argparse

VERSION = "0.1"

# read command line arguments
parser = argparse.ArgumentParser(description='LukeLisp')

parser.add_argument('--verbose_tokeniser', action='store_true', help='Verbose tokeniser')
parser.add_argument('--verbose_parser', action='store_true', help='Verbose parser')
parser.add_argument('-i', action='store_true', help='Launch REPL')

args = parser.parse_args()

def runRepl():
    env = getStandardEnv()
    
    print "LukeLisp " + VERSION
    while(True):
        program = raw_input("LukeLisp: ")
        ast = parse(program, (args.verbose_tokeniser, args.verbose_parser))
        print evaluate(ast, env)

if(args.i):
    runRepl()        
