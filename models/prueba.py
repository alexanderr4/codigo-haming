import random
import copy
from models.data import Data

class Hamming:
    def __init__(self) -> None:
        self.list_position=[]
        self.value_parity = None
    # Función para calcular la paridad (par o impar) de un número binario
    def calcular_paridad(self):
        paridad = self.list_binary.count('1') % 2
        return '1' if paridad == 0 else '0'

    # indentificar las posiciones de los bist de redundancia
    # define la cantidad de bits de redundancia y genera las posicones donde iran esos bits aplicando 2^n
    def redundant_bits(self, datos):
        datos = datos if len(datos) == 7 else ('0'+datos)
        d = len(datos)
        j=0
        r = 1  # Número de bits redundantes
        k = d  # Número de bits de datos
        while 2**r < d + r + 1:
            r += 1
        mi_lista = [None] * (d+r) # 11 posiciones
        for i in range (len(mi_lista)):
            if(i < 4):
                mi_lista[(2**i)-1] = f"p{2**i}"
        for i in range (len(mi_lista)-1,-1,-1):
            if(mi_lista[i] == None):
                mi_lista[i] = datos[j]
                j+=1
        return mi_lista

    #composicion de bits de redundacia
    #devulve las posiciones de bits con las cuales posterioemnte se definira la paridad de los bits de redudancia
    def positionData(self, lista):
        lista2=[]
        m=2
        for i in range (len(lista)):
            if(not(lista[i] == '1' or lista[i] == '0')):
                lista3=[]
                for j in range (i, len(lista),m):
                    if(lista[i] == 'p1'):
                        lista3.append(j+1)
                    elif(lista[i]== 'p2'):
                        lista3.append(j+1)
                        lista3.append(j+2)
                    elif(lista[i]== 'p4' or lista[i]== 'p8'):
                        lista3.append(j+1)
                        lista3.append(j+2)
                        lista3.append(j+3)
                        lista3.append(j+4)
                        break
                lista3[0]=lista[i]
                lista2.append(lista3)
                m+=2
        self.list_position = lista2
        return lista2

    #junto con el metodo vlue_paridad definen la paridad para cada uno de los bits de redundancia
    # teniendo en cuenta las pociones que devuelve le metodo positionData
    def parity(self, listgloba, list1):
        count = 0
        for i in range(len(list1)):
            listgloba = self.assign_parity(listgloba, list1[i])
        return listgloba

    def assign_parity(self, list_global, list):
        bits_activos = 0
        for i in range (1,len(list)):
            if(list_global[list[i]-1] == '1'):
                bits_activos +=1
            if(int(self.value_parity)==0):
                list_global[int(list[0][1])-1] = '0' if bits_activos % 2==0 else '1'
            else:
                list_global[int(list[0][1])-1] = '0' if bits_activos % 2>0 else '1'
        return list_global

    #se genera la posicion alatoria donde va estar el error
    # evitando las posiciones de los bits de redundancia
    def generate_random_error(self, send_list):
        random_position = random.randint(0, len(send_list)-1)
        values = []
        for i in range(len(self.list_position)):
            values.append(int(self.list_position[i][0][1])-1)
        while True:
            random_position = random.randint(0, len(send_list) - 1)
            if random_position not in values:
                break
        send_list[random_position] = '1' if send_list[random_position] =='0' else '0'
        #return ['0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1']
        print(send_list)
        return send_list

    # dectecta el error y la posicion donde se encuentra el error
    def detect_error(self, list_global):
        listaux = copy.deepcopy(self.list_position)
        bits_activos, count, result = 0, 0 ,0
        for j in listaux:
            j[0] = int(j[0][1])
            for i in range(len(j)):
                if(list_global[j[i]-1] == '1'):
                    bits_activos +=1
            if(int(self.value_parity)==0):
                result += 2 ** count if ('0' if bits_activos % 2==0 else '1') == '1' else 0
            else:
                result += 2 ** count if ('0' if bits_activos % 2>0 else '1') == '1' else 0
            count +=1
            bits_activos = 0
        return result

    #corrige el error
    def correct_error(self, list_Global, position):
        list_Global[position-1] = '1' if list_Global[position-1] =='0' else '0'
        return list_Global

"""m = Hamming()
#j=m.calcular_paridad()

p=m.redundant_bits(Data('Z').convertTextBynary()[0])
x= m.positionData(p)
print(x)
aux=m.parity(p, x)
print(aux)
error =  m.generate_random_error(p)


print(m.detect_error(['0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1']))"""

#['1', '1', '0', '1', '1', '0', '1', '1', '1', '0', '1']