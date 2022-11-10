from matplotlib import pyplot as py
from math import tan

i = -1.5
X = []
Y = []

xa = [-5, 5]
ya = [-5, 5]
a = [0, 0]

while i <= 1.5:
    X.append(i)
    Y.append(tan(i))

    i += 0.00001

py.plot(X, Y, "g--", label=" tanX")
py.plot(xa, a, label=" X axis ")
py.plot(a, ya, label=" Y axis ")
py.legend()
py.show()
