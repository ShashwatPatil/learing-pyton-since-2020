
import random
import matplotlib.pyplot as plot
X = []
Y = []
Z = []
F = []
for a in range(100):
    x = (random.random() * 100)
    X.append(x)
for b in range(100):
    y = (random.random() * 100)
    Y.append(y)
for c in range(100):
    z = (random.random() * 100)
    Z.append(z)
for d in range(100):
    f = (random.random() * 100)
    F.append(f)
plot.plot(X, Y, Z, F)
plot.plot(X, Z, Y, F)
plot.plot(F, Y, Z, X)
plot.plot(Z, Y, X, F)
plot.plot(Y, X, F, Z)
plot.plot(Z, X, F, Y)
plot.show()
