import tkinter as Tk
from model.models import Model
from View.views import View
class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Ejemplo de MVC")
        self.root.mainloop()
    def btnHandler(self,event):
        self.action()
    def action(self):
        self.view.ViewPanel; Entry.insert(self.model.saludar())
        