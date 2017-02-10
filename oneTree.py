from common import *

class lSystem(object):
    def __init__(self, rules):
        self.res = rules #cutRandomString(rules)

    def run(self, left, right, forward):
        return manyTrees(self.res, left, right, forward)

def oneBushyTree():
    plant = tree.bushyTree(5)
    lSystem(plant).run(25,25,5)

def oneTwiggyTree():
    plant = tree.twiggyTree(7)
    lSystem(plant).run(25,25,2)

def oneBush():
    plant = tree.bushes(6)
    lSystem(plant).run(25,25,3)

def oneClimber():
    plant = tree.climber(4)
    lSystem(plant).run(27,27,4)

def oneConiferLikeTree():
    plant = tree.coniferLikeTree(12)
    lSystem(plant).run(20,20,11)

def setup(rules, leftAngle, rightAngle, forward, wid):
    tlist = list()
    generators = list()
    for i in range(len(wid)):
        tlist.append(Turtle())
        tlist[i].color(randColor())
        tlist[i].hideturtle()
        tlist[i].tracer(1e3,0)
        tlist[i].left(90)
        tlist[i].penup()
        tlist[i].goto(wid[i], -window_height()/2)
        tlist[i].pendown()
        generators.append(drawTree(rules, tlist[i], leftAngle, rightAngle, forward))

    suma = 0
    while suma < len(wid):
        for n in range(len(wid)):
            suma += next(generators[n],1)
        pass

def manyTrees(rules, leftAngle, rightAngle, forward):
    Screen().bgcolor("#DCF3F3")
    wid = [0]
    setup(rules, leftAngle, rightAngle, forward, wid)

    exitonclick()
