import tkinter 
from tkinter import IntVar

root=tkinter.Tk()
root.title("Radio button basico")
root.iconbitmap("gas.ico")
root.geometry('350x350')
root.resizable(0,0)

def crear_etiqueta():
	#imprimir pantalla
	if number.get() == 1:
		num_label =tkinter.Label(output_frame, text="1 uno 1")
	if number.get() == 2:
		num_label =tkinter.Label(output_frame, text="2 dos 2")
	if number.get() == 3:
		num_label =tkinter.Label(output_frame, text="3 tres 3")
	num_label.pack()    
    


#definicion de frame
input_frame =tkinter.LabelFrame(root, text="esto funciona", width=350, height=100)
output_frame =tkinter.Frame(root, width=350, height=250)
input_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=(0,10))


number =IntVar()
number.set(1)
radio_1 =tkinter.Radiobutton(input_frame, text="Imprimir el nro uno", variable=number, value=1)
radio_2 =tkinter.Radiobutton(input_frame, text="Imprimir el nro dos", variable=number, value=2)
radio_3 =tkinter.Radiobutton(input_frame, text="Imprimir el nro tres", variable=number, value=3)
print_button = tkinter.Button(input_frame, text="Imprimir numero", command=crear_etiqueta)
radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
radio_3.grid(row=1, column=1, padx=10, pady=10)
print_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
