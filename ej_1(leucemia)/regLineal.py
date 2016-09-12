__author__ = 'Jorge Monardes'

""" Regresión Linear para 72 pacientes con Leucemia """

from mymethods import *                       # Importar script de funciones para E-T (Extract - Transform) de Data

# Importamos el resto de librerías necesarias para nuestro modelo
from sklearn import linear_model
import matplotlib.pyplot as plt

# Paso_1: Con las funciones creadas en mymethods.py generamos matrices X y vector y
# Dividiendo dicha data en un set de entrenamiento del modelo (train) y un set de prueba del modelo (test)

train_f = open("train.txt", "r")
train_x = file_to_matrix(train_f)
train_f.close()

test_f = open("test.txt", "r")
test_x = file_to_matrix(test_f)
test_f.close()

samples_f = open("samples.txt", "r")
y = file_to_y(samples_f)
samples_f.close()

y = y_array(y, 'ALL', 'AML')
train_y = y[0:38]
test_y = y[38:]

# Paso_2: Creamos objeto (nuestro modelo) de regresión lineal multi-variable
ols = linear_model.LinearRegression(fit_intercept=False)
ols.fit(train_x, train_y)           # Ajustamos modelo con datos de entrenamiento

# Paso_3: Revisamos resultados estadísticos significativos
# 1. Suma residual de diferencias cuadradas
# 2. Puntaje de varianza, donde "0" indica que el modelo no es mejor que la suerte para obtener resultados,
# "1" indica que el modelo de predicción es perfecto, y valores "negativos" indica que el modelo es peor
# que la suerte.
print("Residual sum of squares: %.2f" % np.sum((ols.predict(test_x) - test_y) ** 2))
print('Variance score: %.2f' % ols.score(test_x, test_y))

# Paso_4: Visualizamos nuestro resultado utilizando matplotlib
axis_x = [i for i in range(0,len(test_y))]
sep_y = [0 for i in range(0,len(test_y))]
plt.plot(axis_x, sep_y, color='black', linewidth=2)
plt.scatter(axis_x, test_y, color='r', alpha=.5, s=100, label='y-test data real')
plt.scatter(axis_x, ols.predict(test_x), color='b', marker='+', s=60, label='y-test predicción del modelo')
plt.xlabel('muestras (pacientes)')
plt.ylabel('Clasificación de Leucemia -- ALL (abajo) | AML (arriba)')
plt.title('Modelo de regresión Lineal Multi-variable', fontsize=18, fontweight='bold')
plt.axis('tight')
plt.grid(True)
plt.ylim(-2, 2)
plt.savefig("regLineal.png")          # Guardamos gráfico en archivo *.png
plt.legend()
plt.show()