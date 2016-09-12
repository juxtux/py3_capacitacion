__author__ = 'Jorge Monardes'

""" Regresión Logística para 72 pacientes con Leucemia  """


from mymethods import *                     # Importar script de funciones para E-T (Extract - Transform) de Data

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

# Paso_2: Creamos objeto (nuestro modelo) de regresión logística multi-variable
lreg = linear_model.LogisticRegression(penalty='l2', C=1e-5, fit_intercept=False, max_iter=100)
# @Parametros:
# penalty: tipo de norma (módulo) utilizada en el penalización.
# C: Intensidad inversa de la regularización. Debe ser un float y valores pequeños ajustan una fuerte regularización.
# fit_intercept: Regresión no necesariamente debe pasar por el cero.
# max_iter: Número máximo de iteraciones por las que pasa el modelo para ajuste de sus parámetros.
lreg.fit(train_x, train_y)

# Paso_3: Revisamos resultados estadísticos significativos
# 1. Suma residual de diferencias cuadradas
# 2. Puntaje de varianza, donde "0" indica que el modelo no es mejor que la suerte para obtener resultados,
# "1" indica que el modelo de predicción es perfecto, y valores "negativos" indica que el modelo es peor
# que la suerte.
print("Residual sum of squares: %.2f" % np.sum((lreg.predict(test_x) - test_y) ** 2))
print('Variance score: %.2f' % lreg.score(test_x, test_y))


# Paso_4: Visualizamos nuestro resultado utilizando matplotlib
axis_x = [i for i in range(0, len(test_y))]
sep_y = [0 for i in range(0, len(test_y))]
plt.plot(axis_x, sep_y, color='black', linewidth=2)
plt.scatter(axis_x, test_y, color='r', alpha=.5, s=100, label='y-test data')
 # Visualización de la predicción sobre la data de test
plt.scatter(axis_x, lreg.predict(test_x), color='b', marker='+', s=60, label='y-test prediction')
plt.xlabel('samples (patients)')
plt.ylabel('Leukemia Classification -- ALL (down) | AML (up)')
plt.title('Logistic Regression | Inv Regularization Strength = 1e-5', fontweight='bold')
plt.axis('tight')
plt.grid(True)
plt.ylim(-2, 2)
plt.legend()
plt.show()
