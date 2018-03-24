# TODO read from a file maybe?  so you can map certain variables into
# the language e.g. a file path or a constant
def getStandardEnv():
    standardEnv = {}

    standardEnv['+'] = lambda x,y:x+y
    standardEnv['-'] = lambda x,y:x-y
    standardEnv['*'] = lambda x,y:x*y
    standardEnv['/'] = lambda x,y:x/y

    standardEnv['pi'] = 3.1415
    
    return standardEnv
