def twiggyTree(n, result='X'):
    for _ in range(n):
        result = result.replace('F', 'FF')
        result = result.replace('X', 'F-[[X]+X]+F[+FX]-X')
    return result

def bushyTree(n, result='F'):
    for _ in range(n):
        result = result.replace('F', 'FF-[-F+F+F]+[+F-F-F]')
    return result

def bushes(n, result='F'):
    for _ in range(n):
        result = result.replace('F', 'FF-[-F+F]+[+F-F]')
    return result

def climber(n, result='F'):
    for _ in range(n):
        result = result.replace('F','FF[-F++F][+F--F]++F--F')
    return result

def coniferLikeTree(n, result='I'):
    for _ in range(n):
        result = result.replace('I', 'VZFFF')
        result = result.replace('V', '[+++W][---W]YV')
        result = result.replace('W', '+X[-W]Z')
        result = result.replace('X', '-W[+X]Z')
        result = result.replace('Y', 'YZ')
        result = result.replace('Z', '[-FFF][+FFF]F')
        result = result.replace('F', 'F')
    return result
