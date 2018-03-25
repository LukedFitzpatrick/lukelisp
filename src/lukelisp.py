from parser import *
from environment import *
from eval import *
import argparse

VERSION = "0.1"

# read command line arguments
parser = argparse.ArgumentParser(description='LukeLisp')

parser.add_argument('file_name', nargs='?', help='.ll File to run')
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


def runFile(fileName):
    print "Evaluating file " + fileName
    
    with open(args.file_name, 'r') as inputFile:
        program = inputFile.readlines()

    env = getStandardEnv()
    for line in program:
        ast = parse(line, (args.verbose_tokeniser, args.verbose_parser))
        result = evaluate(ast, env)

        if isinstance(result, PrintVal):
            print result
    

if(args.i):
    runRepl()        
elif(len(args.file_name) > 0):
    runFile(args.file_name)

