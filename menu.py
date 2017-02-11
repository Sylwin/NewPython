from Tkinter import *
import multipleTree as many
import oneTree as one
import treesRules as tr

class windowFrame(object, Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (startWindow, bushyTreeFrame, twiggyTreeFrame, bushesFrame, climberFrame, coniferLikeTreeFrame):
            pageName = F.__name__
            frame = F(container, self)
            self.frames[pageName] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("startWindow")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()

    def button(self, obj, msg, com, color="green", wid = 30, hei = 2, border = 3):
        b = Button(obj, text=msg, width=wid, height=hei, bd=border, activeforeground=color, command=com)
        b.pack(fill=BOTH, expand=True, padx=20, pady=5)
        return b

class startWindow(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        a = controller.button(self, "Bushy Tree", lambda: controller.showFrame("bushyTreeFrame"))
        b = controller.button(self, "TwiggyTree", lambda: controller.showFrame("twiggyTreeFrame"))
        c = controller.button(self, "Bushes", lambda: controller.showFrame("bushesFrame"))
        e = controller.button(self, "Climber", lambda: controller.showFrame("climberFrame"))
        d = controller.button(self, "Conifer-like Tree", lambda: controller.showFrame("coniferLikeTreeFrame"))
        f = controller.button(self, "Exit", lambda: root.destroy(), "red")

class bushyTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.bushyTree,5) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.bushyTree,4) )
        r = controller.button(self, "Back", lambda: controller.showFrame("startWindow"), "red")

class twiggyTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.twiggyTree,7) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.twiggyTree,6) )
        r = controller.button(self, "Back", lambda: controller.showFrame("startWindow"), "red")

class bushesFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.bushes,6) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.bushes,5) )
        r = controller.button(self, "Back", lambda: controller.showFrame("startWindow"), "red")

class climberFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.climber,4) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.climber,4) )
        r = controller.button(self, "Back", lambda: controller.showFrame("startWindow"), "red")

class coniferLikeTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.coniferLikeTree,6) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.coniferLikeTree,5) )
        r = controller.button(self, "Back", lambda: controller.showFrame("startWindow"), "red")

if __name__ == "__main__":
    root = windowFrame()
    root.mainloop()
