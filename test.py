import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Botón con Esquinas Redondeadas")

    # Crea un botón con esquinas redondeadas
    boton = tk.Button(ventana, text="Botón Redondeado", relief="groove", borderwidth=10)
    boton.pack(pady=50)

    ventana.mainloop()

crear_ventana()
