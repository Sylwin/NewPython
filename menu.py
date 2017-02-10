from Tkinter import *
import multipleTree as many
import oneTree as one

#from turtle import *
#bye()

def button(obj, msg, com, color="green", wid = 30, hei = 2, border = 3):
    b = Button(obj, text=msg, width=wid, height=hei, bd=border, activeforeground=color, command=com)
    b.pack(fill=BOTH, expand=True, padx=20, pady=5)
    return b

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        a = button(self, "Bushy Tree", lambda: self.choice(one.oneBushyTree, many.manyBushyTrees, "Bushy Tree"))
        b = button(self, "TwiggyTree", lambda: self.choice(one.oneTwiggyTree, many.manyTwiggyTrees,  "Twiggy Tree"))
        c = button(self, "Conifer-like Tree", lambda: self.choice(one.oneConiferLikeTree, many.manyConiferLikeTrees, "Conifer-like Tree"))
        d = button(self, "Bushes", lambda: self.choice(one.oneBush, many.manyBushes, "Bushes"))
        e = button(self, "Climber", lambda: self.choice(one.oneClimber, many.manyClimbers,  "Climber"))
        f = button(self, "Exit", root.quit, "red")

    def choice(self, sTree, mTree, name):
        top = Toplevel(self)
        top.title(name)
        b = button(top, "Single", sTree)
        c = button(top, "Many", mTree)
        r = button(top, "Close", top.destroy, "red")

if __name__ == "__main__":
    root = Tk()
    root.title('Menu')
    MainWindow(root).pack(fill="both", expand=True)
    root.mainloop()
