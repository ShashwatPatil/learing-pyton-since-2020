from matplotlib import pyplot as py
from math import sin

i = -10
X = []
Y = []

while i <= 10:
    if i == 0:
        pass
    else:
        X.append(i)
        Y.append(sin(i) / i)
        i += 0.01
 
py.plot(X, Y, label=" (sinX)/x")
py.legend()
py.show()
