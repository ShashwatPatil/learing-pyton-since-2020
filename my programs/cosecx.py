from matplotlib import pyplot as py
from math import sin, pi

i = -(3*pi) + 0.5

X = []
Y = []

xa = [-10, 10]
a = [0, 0]

while i <= (3*pi) - 0.5:
    if -0.1 < i < 0.1 or -0.1 - pi < i < 0.1 - pi or -0.1 - (2 * pi) < i < 0.1 - (2 * pi) or -0.1 + (2 * pi) < i < 0.1 + (2 * pi) or -0.1 + pi < i < 0.1 + pi:
        pass
    else:
        X.append(i)
        Y.append(1/(sin(i)))

    i += 0.00001

py.plot(X, Y, "g--", label=" cosec X")
py.plot(xa, a, label=" X axis ")
py.plot(a, xa, label=" Y axis ")
py.legend()
py.show()
