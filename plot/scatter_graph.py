import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets


iris = datasets.load_iris()

data = iris.data
label = iris.target


x = data.T[0]
y = data.T[1]
z = data.T[2]

fig = plt.figure()
ax1 = Axes3D(fig)

ax1.scatter(x, y, z, c=label)

plt.show()