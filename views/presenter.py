import tkinter as tk
from cotrolers import controler

class GeneradorMatricesApp:
    hola = ''
    def __init__(self, root, control):
        self.control= control
        self.root = root
        self.root.title("Código de Hamming")

        # Etiqueta para ingresar la cadena
        self.etiqueta = tk.Label(self.root, text="Ingrese una cadena de texto:")
        self.etiqueta.pack()

        # Entrada de texto
        self.entrada_texto = tk.Entry(self.root)
        self.entrada_texto.pack()



        # Botón para mostrar las matrices
        self.boton_mostrar = tk.Button(self.root, text="Mostrar Matrices", command=self.mostrar_matrices)
        self.boton_mostrar.pack()


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
            # Crear la matriz como una lista de listas
            #matriz = [[' ' for _ in range(ancho)] for _ in range(ancho)]

            # Llenar la primera posición de cada fila con las letras de la cadena
            """for i in range(ancho):
                matriz[i][0] = cadena[i]"""

            # Crear una representación de cadena de la matriz
            matriz_texto = '\n'.join([' '.join(fila) for fila in matriz])

            # Mostrar la matriz en la etiqueta
            matriz_label.config(text=matriz_texto)

    def entrada(self):
        return self.entrada_texto.get()
    def mostrar_matrices(self):
        texto = self.entrada_texto.get()

        self.generar_matriz(texto, self.frame1, "cadena", self.matriz(texto))
        self.generar_matriz(texto, self.frame2, "A ser recibida(ERRORES)", self.control.generate_data_burst_matrix(texto))
        self.generar_matriz(texto, self.frame3, "A ser recibida(CORREGIDA)", self.control.generate_error_matrix())
        self.generar_matriz(texto, self.frame4, "A ser recibida(CORREGIDA)", self.control.error_detection_and_correction())

    def matriz(self, text):
        resul=[]
        text = list(text)
        for i in range(0, len(text)):
            resul.append(text[i])
        return resul