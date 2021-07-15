import tkinter as tk

from model.models import Model
from View.views import View

class Controller():
    def __init__ (self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Ejemplo de MVC")
        self.root.mainloop()
    def btnHandler (self, event):
        self.action()

    def action(self):
        self.view.viewPanel.entry.insert(0,self.model.saludar())