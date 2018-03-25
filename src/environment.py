# TODO read from a file maybe?  so you can map certain variables into
# the language e.g. a file path or a constant
def getStandardEnv():
    standardEnv = {}

    standardEnv['+'] = lambda x,y:x+y
    standardEnv['-'] = lambda x,y:x-y
    standardEnv['*'] = lambda x,y:x*y
    standardEnv['/'] = lambda x,y:x/y

    standardEnv['>'] = lambda x,y:x>y
    standardEnv['<'] = lambda x,y:x<y
    standardEnv['>='] = lambda x,y:x>=y
    standardEnv['<='] = lambda x,y:x<=y

    standardEnv['='] = lambda x,y:x==y
    
    standardEnv['not'] = lambda x:not x
    standardEnv['and'] = lambda x,y:x and y
    standardEnv['or'] = lambda x,y:x and y

    standardEnv['t'] = True
    standardEnv['true'] = True
    standardEnv['f'] = False
    standardEnv['false'] = False

    standardEnv["str"] = lambda x: str(x)
    standardEnv["int"] = lambda x: int(x)
    standardEnv["float"] = lambda x: float(x)
    
    standardEnv['pi'] = 3.1415
    
    return standardEnv
