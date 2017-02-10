from common import *

class lSystem(object):
    def __init__(self, rules):
        self.res = rules

    def run(self, left, right, forward):
        return manyTrees(self.res, left, right, forward)

def manyBushyTrees():
    plant = tree.bushyTree(4)
    lSystem(plant).run(25,25,5)

def manyTwiggyTrees():
    plant = tree.twiggyTree(6)
    lSystem(plant).run(25,25,2)

def manyBushes():
    plant = tree.bushes(5)
    lSystem(plant).run(25,25,4)

def manyClimbers():
    plant = tree.climber(4)
    lSystem(plant).run(27,27,4)

def manyConiferLikeTrees():
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
        res = cutRandomString(rules)
        generators.append(drawTree(res, tlist[i], leftAngle, rightAngle, forward))

    suma = 0
    while suma < len(wid):
        for n in range(len(wid)):
            suma += next(generators[n],1)
        pass


def manyTrees(rules, leftAngle, rightAngle, forward):
    Screen().bgcolor("#DCF3F3")
    wid = [x for x in range(-500,501,85)]
    setup(rules, leftAngle, rightAngle, forward, wid)

    exitonclick()
