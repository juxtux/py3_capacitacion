__author__ = 'Jorge Monardes'

import numpy as np
import matplotlib.pyplot as plt

test_y = np.random.uniform(-1, 1, 36)
real_y = np.random.uniform(-1, 1, 36)
axis_x = [i for i in range(0,len(test_y))]
sep_y = [0 for i in range(0,len(test_y))]


plt.plot(axis_x, sep_y, color='black',
         linewidth=2)
plt.scatter(axis_x, test_y, color='r',
            alpha=.5, s=100,
            label='y-test data real')
plt.scatter(axis_x, real_y,
            color='b', marker='+', s=60,
            label='y-test predicción del modelo')

plt.xlabel('muestras (pacientes)')
plt.ylabel('Clasificación de Leucemia -- '
           'ALL (abajo) | AML (arriba)')
plt.title('Modelo de regresión Lineal Multi-variable',
          fontsize=18, fontweight='bold', loc='center')

plt.axis('tight')
plt.grid(True)
plt.ylim(-2, 2)
plt.savefig("myPlot.png")
plt.legend(loc='best')

plt.show()


