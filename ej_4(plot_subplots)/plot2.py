__author__ = 'Jorge Monardes'

"""
Esta es una adaptación del script original de
http://matplotlib.org/examples/statistics/
histogram_demo_multihist.html
para ilustrar principales componentes de
sub-gráficos en Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

n_bins = 10
x = np.random.randn(1000, 3)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flat

colors = ['red', 'tan', 'lime']
ax0.hist(x, n_bins, normed=1, histtype='bar',
         color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('barras con legenda')

ax1.hist(x, n_bins, normed=1, histtype='bar',
         stacked=True)
ax1.set_title('barras stacked')

ax2.hist(x, n_bins, histtype='step',
         stacked=True, fill=True)
ax2.set_title('stepfilled')

# Make a multiple-histogram of
# data-sets with different length.
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('diferentes tamaños de muestra')

plt.tight_layout()
plt.show()

