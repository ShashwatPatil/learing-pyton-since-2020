from matplotlib import pyplot as py
from math import log10

i = 0.01
X = []
Y = []
xa = [-10, 10]
ya = [-10, 10]
a = [0, 0]

while i <= 10:
    X.append(i)
    Y.append(log10(i))

    i += 0.001

py.plot(X, Y, "g--", label=" log10X")
py.plot(xa, a, label=" X axis ")
py.plot(a, ya, label=" Y axis ")
py.legend()
py.show()
