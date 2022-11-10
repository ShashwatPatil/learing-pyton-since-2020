from matplotlib import pyplot as py
from math import sin

i = -10
j = -10
k = -10
X = []
Y = []
X1 = []
Y1 = []
X2 = []
Y2 = []

xa = [-10, 10]
ya = [-10, 10]
a = [0, 0]

while i <= 10:
    X.append(i)
    Y.append(sin(i))

    i += 0.001

while j <= 10:
    X1.append(j)
    Y1.append(sin(2*j))

    j += 0.001

while k <= 10:
    X2.append(k)
    Y2.append(sin(k/2))

    k += 0.001

py.plot(X, Y, "g--", label=" sinX")
py.plot(X1, Y1, label=" sin 2X")
py.plot(X2, Y2, label=" sin X/2")
py.plot(xa, a, label=" X axis ")
py.plot(a, ya, label=" Y axis ")
py.legend()
py.show()
