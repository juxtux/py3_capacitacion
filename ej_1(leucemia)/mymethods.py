__author__ = 'Jorge Monardes'

""" Script con cuatro funciones de interés para el análisis de pacientes con Leucemia: """

# importamos librería Numpy:
import numpy as np

# is_number(s) prueba si la variable "s" (comúnmente un string) puede ser transformada a una variable número.
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# file_to_matrix(file_x) toma el puntero del archivo "file_x" y construye matriz de variables X que utilizarán
# nuestros modelos
def file_to_matrix(file_x):
    r_list = list()

    while 1:
        rows = file_x.readline()
        if not rows or rows == '\n':
            break
        rows = rows.strip().split('\t')
        row = [float(num) for num in rows if is_number(num)]
        r_list.append(row)

    r_array = np.array(r_list)
    r_array = np.transpose(r_array)
    return np.delete(r_array,0,1)           # delete row[0] <=> header label

# file_to_y(file_y) toma puntero del archivo "file_y" y construye lista de pacientes con tipo ALL/AML
def file_to_y(file_y):
    r_list = []
    while 1:
        row = file_y.readline()
        if not row:
            break
        if is_number(row[0:2]):
            row_s = row.split('\t\t')
            result = row_s[1].strip()
            r_list.append([int(row[0:2]), result])
    return r_list

# y_array(y, zero, ones) toma lista "y" y la convierte ALL/AML en binario, utilizando valores definidos en
# variables zeros y ones. En este script fijamos zeros = -1 y ones = 1.
def y_array(y, zeros, ones):
    r_array = [-1 if tuple[1] == zeros else 1 if tuple[1] == ones else 'error_value' for tuple in y]
    return np.array(r_array)

"""Leer control flow interno de r_array como:
for tuple in y:
    if tuple[1] == zeros:
        return -1
    else:
        if tuple[1] == ones:
            return +1
        else:
            return 'error_value'

"""