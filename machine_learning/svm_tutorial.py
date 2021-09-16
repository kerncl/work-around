print(__doc__)


import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm


iris = datasets.load_iris()

x = iris.data
y = iris.target

x = x[y != 0, :2]
y = y[y != 0]

n_sample = len(x)

np.random.seed(0)
order = np.random.permutation(n_sample)
x = x[order]
y = y[order].astype(float)

x_train = x[:int(.9* n_sample)]
y_train = y[:int(.9*n_sample)]
x_test = x[:int(.9*n_sample)]
y_test = y[:int(.9*n_sample)]

# fit the model
for kernel in ('linear', 'rbf', 'poly'):
    clf = svm.SVC(kernel=kernel, gamma=10)
    clf.fit(x_train, y_train)

    plt.figure()
    plt.clf()
    plt.scatter(x[:, 0], x[:, 1], c=y, zorder=10, cmap=plt.cm.Paired, edgecolors='k', s=20)

    # circle out the test data
    plt.scatter(x_test[:, 0], x_test[:,1], s=80, facecolors='none', zorder=10, edgecolors='k')

    plt.axis('tight')
    x_min = x[:, 0].min()
    x_max = x[:, 0].max()
    y_min = x[:, 1].min()
    y_max = x[:, 1].max()

    xx, yy = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    z = clf.decision_function(np.c[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    z = z.reshape(xx.shape)
    plt.pcolormesh(xx, yy, z>0, cmap=plt.cm.Paired)
    plt.contour(xx, yy, z, colors=['k', 'k', 'k'], linestyle=['--', '-', '--'], levels=[-.5, 0, .5])
    plt.title(kernel)
plt.show()