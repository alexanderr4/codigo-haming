from models import data, prueba
from views import view
import tkinter as tk

class Controler:

    def __init__(self):
        self.text = ''
        self.hamming = prueba.Hamming()
        self.list_send = []
        self.detect_error = []


    # Iniciar la aplicación GeneradorMatricesApp
    def text_binary(self, text):
        self.text = text
        return data.Data(self.text).convertTextBynary()


    #genera la mtriz rafaga a ser enviada
    def generate_data_burst_matrix(self, text, value_parity):
        #print(value_parity)
        hamming = self.hamming
        self.hamming.value_parity = value_parity
        list_data_burst_matrix = []
        for i in range(len(text)):
            bit_redundancy = hamming.redundant_bits(self.text_binary(text)[i])
            composicion_de_bits_de_redundacia = hamming.positionData(bit_redundancy)
            parity_values = hamming.parity(bit_redundancy, composicion_de_bits_de_redundacia)
            list_data_burst_matrix.append(parity_values)
        self.list_send=list_data_burst_matrix
        return list_data_burst_matrix

    #genera las mtrices con lo errores aleatorios para acda caracter
    def generate_error_matrix(self):
        hamming = self.hamming
        list_matrix_error = []
        for i in range(len(self.list_send)):
            error = hamming.generate_random_error(self.list_send[i])
            print(error)
            print()
            list_matrix_error.append(error)
        print(list_matrix_error)
        self.detect_error = list_matrix_error
        return list_matrix_error

    def error_detection_and_correction(self):
        list_detect_error = []
        list_error_position =[]
        error_position = None
        hamming = self.hamming
        for i in range(len(self.detect_error)):
            error_position = hamming.detect_error(self.detect_error[i])
            list_error_position.append(error_position)
            list_detect_error.append(hamming.correct_error(self.detect_error[i],error_position))
        print(list_error_position)
        return list_detect_error
    def errors_position(self):
        list_detect_error = []
        hamming = self.hamming
        print(self.detect_error)
        for i in range(len(self.detect_error)):
           list_detect_error.append(hamming.detect_error(self.detect_error[i]))
        return list_detect_error

"""m = Controler()
print(m.generate_data_burst_matrix('Hz'))
print(m.generate_error_matrix())
print(m.error_detection_and_correction())
print(m.errors_position())"""