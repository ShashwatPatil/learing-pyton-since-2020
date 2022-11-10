from matplotlib import pyplot as py
from math import exp

i = -3
X = []
Y = []
xa = [-10, 10]
ya = [-10, 10]
a = [0, 0]

while i <= 3:
    X.append(i)
    Y.append(exp(i))

    i += 0.001

py.plot(X, Y, "g--", label=" e^x")
py.plot(xa, a, label=" X axis ")
py.plot(a, ya, label=" Y axis ")
py.legend()
py.show()
