__author__ = 'Jorge Monardes'
import numpy as np
# from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn import svm

""" Data: Loaded from sklearn datasets """
iris_plant = datasets.load_iris()
X = iris_plant.data
y = iris_plant.target
X_train = X[:, 0:3]
X1, X2, X3 = X_train[:50], X_train[50:100], X_train[100:150]
y1, y2, y3 = y[:50], y[50:100], y[100:150]

""" 3D Meshgrid: """
line_space = np.linspace(0, 9, 20)
line_space = np.around(line_space, decimals=2)
xy, xz = np.meshgrid(line_space, line_space)
for z in line_space:
    xy_z = np.c_[np.ravel(xy), np.ravel(xz)]
    xy_z = np.insert(xy_z, 2, z, axis=1)
    space3D = xy_z if z == 0 else np.append(space3D, xy_z, axis=0)


""" SVM: """
C = 1.0     # SVM regularization parameter
svm1 = svm.SVC(kernel='linear', C=C).fit(X_train, y)

y_hat1 = svm1.predict(space3D)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X3[:, 0], X3[:, 1], X3[:, 2], c='b', label='Virginica')
ax.scatter(X2[:, 0], X2[:, 1], X2[:, 2], c='g', label='Versicolour')
ax.scatter(X1[:, 0], X1[:, 1], X1[:, 2], c='r', label='Setosa')

ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('sepal width (cm)')
ax.set_zlabel('petal length (cm)')

vmax = 3.0
cmap = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'r'),
                                                    (1 / vmax, 'g'),
                                                    (3 / vmax, 'b')]
                                        )
ax.scatter(space3D[:, 0], space3D[:, 1], space3D[:, 2], c=y_hat1, cmap=cmap, marker='s', s=100, alpha=.05)

plt.title('SVM Classification (Linear Kernel) | Regularization: C = 1', fontweight='bold')
plt.legend()
plt.show()