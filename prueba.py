import random

# Función para calcular la paridad (par o impar) de un número binario
def calcular_paridad(bits):
    paridad = bits.count('1') % 2
    return '1' if paridad == 0 else '0'

# Función para insertar errores en la ráfaga de datos
def insertar_errores(datos, posiciones_errores):
    for pos in posiciones_errores:
        if datos[pos] == '0':
            datos = datos[:pos] + '1' + datos[pos+1:]
        else:
            datos = datos[:pos] + '0' + datos[pos+1:]
    return datos

# Función para simular la detección y corrección de errores usando Hamming
def deteccion_correccion(datos, paridad):
    n = len(datos)
    m = 1  # Número de bits redundantes
    k = n  # Número de bits de datos

    while 2**m < n + m + 1:
        m += 1

    datos_codificados = ['0'] * (m + k)
    j = 0

    for i in range(1, m + k + 1):
        if i == 2**j:
            j += 1
        else:
            datos_codificados[i - 1] = datos[j]

    if paridad == 'Even':
        paridad_codificada = [calcular_paridad(bits) for bits in datos_codificados]
    else:
        paridad_codificada = [str(int(not int(bits))) for bits in datos_codificados]

    datos_codificados = ''.join(paridad_codificada)

    # Simulación de errores
    posiciones_errores = random.sample(range(len(datos_codificados)), k)  # Selecciona k posiciones aleatorias
    datos_transmitidos = insertar_errores(datos_codificados, posiciones_errores)

    # Detección de errores
    errores_detectados = [pos for pos in posiciones_errores if datos_transmitidos[pos] != datos_codificados[pos]]

    # Corrección de errores
    for pos in errores_detectados:
        if datos_transmitidos[pos] == '0':
            datos_transmitidos = datos_transmitidos[:pos] + '1' + datos_transmitidos[pos+1:]
        else:
            datos_transmitidos = datos_transmitidos[:pos] + '0' + datos_transmitidos[pos+1:]

    return datos_codificados, datos_transmitidos, errores_detectados

# Datos de entrada
datos_ascii = "Data"
paridad = "Even"  # Puedes cambiar a "Odd" para probar con paridad impar

# Procesar cada letra individualmente
for char in datos_ascii:
    char_binario = ''.join(format(ord(char), '07b'))
    
    # Simulación de detección y corrección de errores
    datos_codificados, datos_transmitidos, errores_detectados = deteccion_correccion(char_binario, paridad)

    # Resultados para la letra actual
    print(f"Letra: {char}")
    print("Datos ASCII:", ord(char))
    print("Datos en binario:", char_binario)
    print("Datos codificados (Hamming):", datos_codificados)
    print("Datos transmitidos con errores:", datos_transmitidos)
    print("Posiciones de errores detectados:", errores_detectados)
    print()

