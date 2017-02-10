from random import *
from turtle import *
import treesRules as tr

def cutRandomString(result):
    leng = len(result)
    beg = randrange(0, leng/2, 1)
    end = randrange(beg, beg+leng/2, 1)
    start = result[:beg]
    finish = result[end:]
    result = start+finish
    return result

def randColor():
    red = randrange(0,100,1)
    green = randrange(150,255,1)
    blue = randrange(0,100,1)
    r = hex(red).split('x')[1]
    g = hex(green).split('x')[1]
    b = hex(blue).split('x')[1]
    if( len(r) < 2 ): r = "0" + r
    if( len(g) < 2 ): g = "0" + g
    if( len(b) < 2 ): b = "0" + b
    col = "#" + r + g + b
    return col

def drawTree(commands, turtle, leftAngle, rightAngle, forwardDistance):
    stack = []
    for cmd in commands:
        if cmd == 'F':
            turtle.forward(forwardDistance)
        elif cmd == '-':
            turtle.left(leftAngle)
        elif cmd == '+':
            turtle.right(rightAngle)
        elif cmd == 'X' or cmd == 'I' or cmd == 'V' or cmd == 'W' or cmd == 'Y' or cmd == 'Z':
            pass
        elif cmd == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd == ']':
            if( len(stack) == 0 ):
                pass
            else:
                position, heading = stack.pop()
                turtle.up()
                turtle.setposition(position)
                turtle.setheading(heading)
                turtle.down()
        else:
            raise ValueError('Unknown cmd: %c' % cmd)
        yield(0)
