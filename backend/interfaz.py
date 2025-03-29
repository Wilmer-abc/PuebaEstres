import tkinter as tk
from tkinter import ttk
from backend.alumnos import agregar_alumno, actualizar_alumno, eliminar_alumno

def interfaz():
    root = tk.Tk()
    root.title("Registro de alumnos")

    tk.Label(root, text="Carnet").pack()
    carnet1 = tk.Entry(root, width=5)
    carnet1.pack()
    carnet2 = tk.Entry(root, width=3)
    carnet2.pack()
    carnet3 = tk.Entry(root, width=5)
    carnet3.pack()

    tk.Label(root, text="Nombre").pack()
    primer_nombre = tk.Entry(root)
    primer_nombre.pack()
    segundo_nombre = tk.Entry(root)
    segundo_nombre.pack()
    primer_apellido = tk.Entry(root)
    primer_apellido.pack()
    segundo_apellido = tk.Entry(root)
    segundo_apellido.pack()

    tk.Label(root, text="Teléfono").pack()
    telefono = tk.Entry(root)
    telefono.pack()

    tk.Label(root, text="Correo").pack()
    correo = tk.Entry(root)
    correo.pack()

    tk.Label(root, text="Pagado").pack()
    pagado = ttk.Combobox(root, values=["Sí", "No"])
    pagado.pack()
    pagado.current(1)

    tk.Label(root, text="Fecha Nacimiento").pack()
    fecha_nacimiento = tk.Entry(root) 
    fecha_nacimiento.pack()

    tk.Button(root, text="Agregar", command=lambda: agregar_alumno(
        carnet1.get(), carnet2.get(), carnet3.get(),
        primer_nombre.get(), segundo_nombre.get(), primer_apellido.get(), segundo_apellido.get(),
        telefono.get(), correo.get(), pagado.get(), fecha_nacimiento.get()  
    )).pack()

    tk.Button(root, text="Actualizar", command=lambda: actualizar_alumno(
        carnet1.get(), carnet2.get(), carnet3.get(),
        primer_nombre.get(), segundo_nombre.get(), primer_apellido.get(), segundo_apellido.get(),
        telefono.get(), correo.get(), pagado.get(), fecha_nacimiento.get()  
    )).pack()

    tk.Button(root, text="Eliminar", command=lambda: eliminar_alumno(
        carnet1.get(), carnet2.get(), carnet3.get()
    )).pack()

    root.mainloop()
