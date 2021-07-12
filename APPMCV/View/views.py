import tkinter as Tk

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = Tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)
        
     
class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller 
        self.framePanel =Tk.Frame(root)
        self.label =Tk.Label(self.framePanel, text="Resultados")
        self.label.pack()
        self.entry = Tk.Entry(self.framePanel)
        self.entry.pack()
        self.btn = Tk.Button(self.framePanel, text ="Saludar")
        self.btn.pack()
        self.btn.bind("<Button>", controller.btnHandler) 