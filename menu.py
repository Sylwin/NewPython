from Tkinter import *
import multipleTree as many
import oneTree as one
import treesRules as tr

class SampleApp(object, Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
       # container.grid_rowconfigure(0, weight=1)
       # container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainWindow, bushyTreeFrame, twiggyTreeFrame, bushesFrame, climberFrame, coniferLikeTreeFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def button(self, obj, msg, com, color="green", wid = 30, hei = 2, border = 3):
        b = Button(obj, text=msg, width=wid, height=hei, bd=border, activeforeground=color, command=com)
        b.pack(fill=BOTH, expand=True, padx=20, pady=5)
        return b

class MainWindow(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        a = controller.button(self, "Bushy Tree", lambda: controller.show_frame("bushyTreeFrame"))
        b = controller.button(self, "TwiggyTree", lambda: controller.show_frame("twiggyTreeFrame"))
        c = controller.button(self, "Bushes", lambda: controller.show_frame("bushesFrame"))
        e = controller.button(self, "Climber", lambda: controller.show_frame("climberFrame"))
        d = controller.button(self, "Conifer-like Tree", lambda: controller.show_frame("coniferLikeTreeFrame"))
        #f = controller.button(self, "Exit", app.quit, "red")

class bushyTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.bushyTree,5) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.bushyTree,4) )
        r = controller.button(self, "Back", lambda: controller.show_frame("MainWindow"), "red")

class twiggyTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.twiggyTree,7) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.twiggyTree,6) )
        r = controller.button(self, "Back", lambda: controller.show_frame("MainWindow"), "red")

class bushesFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.bushes,6) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.bushes,5) )
        r = controller.button(self, "Back", lambda: controller.show_frame("MainWindow"), "red")

class climberFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.climber,4) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.climber,4) )
        r = controller.button(self, "Back", lambda: controller.show_frame("MainWindow"), "red")

class coniferLikeTreeFrame(object, Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        b = controller.button(self, "Single (regular shape)", lambda: one.tree(tr.coniferLikeTree,6) )
        c = controller.button(self, "Many (mutated)", lambda: many.trees(tr.coniferLikeTree,5) )
        r = controller.button(self, "Back", lambda: controller.show_frame("MainWindow"), "red")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
