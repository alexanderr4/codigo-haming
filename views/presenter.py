import tkinter as tk
from PIL import Image, ImageFilter, ImageTk
from tkinter import ttk


from cotrolers import controler

class GeneradorMatricesApp:
    hola = ''
    def __init__(self, root, control):
        self.control= control
        self.root = root
        self.root.title("Código de Hamming")
        self.root.configure(bg='#dceafb')
        self.root.geometry("800x600")  # Establece el tamaño de la ventana a 800x600 píxeles

     

        # Etiqueta para ingresar la cadena
        self.etiqueta = tk.Label(self.root, text="Ingrese una cadena de texto:")
        self.etiqueta.pack()

        # Entrada de texto
        self.entrada_texto = tk.Entry(self.root)
        self.entrada_texto.pack()
        self.entrada_texto.focus_set()

        self.etiqueta_pariedad = tk.Label(self.root, text="Seleccione Paridad:")
        self.etiqueta_pariedad.pack()

        # Crear una lista de opciones para el JComboBox
        opciones = ['0', '1']

        self.paridad_seleccionada = tk.StringVar(value=opciones[0])

        # Crear el JComboBox
        self.combobox_pariedad = tk.OptionMenu(self.root, self.paridad_seleccionada, *opciones)
        self.combobox_pariedad.pack()


        # Botón para mostrar las matrices
        self.boton_mostrar = tk.Button(self.root, text="Mostrar Matrices", command=self.mostrar_matrices)
        self.boton_mostrar.pack()

        # Cambiar el color de fondo y el color del texto del botón
        self.boton_mostrar.config(bg="#004c70", fg="white")

        # Hacer el botón más redondo (ajustar el valor de borderwidth)
        self.boton_mostrar.config(borderwidth=5)

        # Tres frames para mostrar las matrices
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)




    def generar_matriz(self, cadena, frame, nombre, matriz):
        ancho = len(cadena)
        

        # Limpiar el contenido anterior del frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Etiqueta para mostrar el nombre de la matriz
        nombre_label = tk.Label(frame, text=nombre)
        nombre_label.pack()

        # Crear una etiqueta para mostrar la matriz en el frame proporcionado
        matriz_label = tk.Label(frame)
        matriz_label.pack()

        # Mostrar los valores de la cadena solo en la primera matriz (frame1)
        if frame == self.frame1 or frame == self.frame2 or frame == self.frame3 or frame==self.frame4:
            matriz_texto = ''

            # Función para mostrar la matriz con un retraso
            def actualizar_matriz(i=0):
                nonlocal matriz_texto
                if i < ancho:
                    # Agrega una fila de la matriz a la etiqueta
                    fila = ''.join(matriz[i])
                    matriz_texto += fila + '\n'
                    matriz_label.config(text=matriz_texto)

                    # Llama a la función de actualización nuevamente después de un cierto tiempo (aquí, 500 ms)
                    frame.after(500, lambda: actualizar_matriz(i + 1))
                else:
                    # La matriz se ha mostrado por completo
                    frame.after(1000, lambda: matriz_label.config(text=matriz_texto))

            # Inicia la actualización de la matriz
            actualizar_matriz()


    def entrada(self):
        return self.entrada_texto.get()
    def mostrar_matrices(self):
        texto = self.entrada_texto.get()

        self.frame1.configure(bg='lightblue')  # Cambia 'lightblue' al color que prefieras
        self.generar_matriz(texto, self.frame1, "Cadena", self.matriz(texto))

        self.frame2.configure(bg='lightgreen')  # Cambia 'lightgreen' al color que prefieras
        self.generar_matriz(texto, self.frame2, "Matriz a ser transmitida", self.control.generate_data_burst_matrix(texto))

        self.frame3.configure(bg='lightpink')  # Cambia 'lightpink' al color que prefieras
        self.generar_matriz(texto, self.frame3, "Matriz a ser recibida (Errores)", self.control.generate_error_matrix())

        self.frame4.configure(bg='lightyellow')  # Cambia 'lightyellow' al color que prefieras
        self.generar_matriz(texto, self.frame4, "Matriz a ser recibida (Corregida)", self.control.error_detection_and_correction())
    def matriz(self, text):
        resul=[]
        text = list(text)
        for i in range(0, len(text)):
            resul.append(text[i])
        return resul