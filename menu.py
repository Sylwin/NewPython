from Tkinter import *
import multipleTree as many
import oneTree as one
import treesRules as tr

def button(obj, msg, com, color="green", wid = 30, hei = 2, border = 3):
    b = Button(obj, text=msg, width=wid, height=hei, bd=border, activeforeground=color, command=com)
    b.pack(fill=BOTH, expand=True, padx=20, pady=5)
    return b

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        a = button(self, "Bushy Tree", lambda: self.choice(
                   lambda: one.tree(tr.bushyTree,5),
                   lambda: many.trees(tr.bushyTree,4), "Bushy Tree"))
        b = button(self, "TwiggyTree", lambda: self.choice(
                   lambda: one.tree(tr.twiggyTree,7),
                   lambda: many.trees(tr.twiggyTree,6),  "Twiggy Tree"))
        c = button(self, "Bushes", lambda: self.choice(
                   lambda: one.tree(tr.bushes,6),
                   lambda: many.trees(tr.bushes,5), "Bushes"))
        e = button(self, "Climber", lambda: self.choice(
                   lambda: one.tree(tr.climber,4),
                   lambda: many.trees(tr.climber,4),  "Climber"))
        d = button(self, "Conifer-like Tree", lambda: self.choice(
                   lambda: one.tree(tr.coniferLikeTree,6),
                   lambda: many.trees(tr.coniferLikeTree,5), "Conifer-like Tree"))
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
