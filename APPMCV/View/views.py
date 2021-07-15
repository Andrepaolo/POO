import tkinter as tk

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.framePanel = tk.Frame(root)
        self.framePanel.pack()
        self.label = tk.Label(self.framePanel, text="Resultado")
        self.label.pack()
        self.entry = tk.Entry(self.framePanel)
        self.entry.pack()
        self.btn = tk.Button(self.framePanel, text="Saludas")
        self.btn.pack()
        self.btn.bind("<Button>", controller.btnHandler)