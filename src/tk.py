import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso","boton presionado")
   

ventana=tk.Tk()

 

label =tk.Label(ventana, text="precionar el boton para ver el mensaje ")
label.pack(pady=10)

boton=tk.Button(ventana,text="haz click aqui",command=mostrar_mensaje)
boton.pack(pady=10)




ventana.mainloop()#Muestra la ventana