from matplotlib import pyplot as py

r = int(input("Enter the radius of circle:"))

X1 = []
Y1 = []
X2 = []
Y2 = []
X = []
Y = []
for x in range(-100*r, 100*r, 1):
    R = r * r
    a = x * x / 10000
    y1 = (R - a) ** 0.5
    X1.append(x/100)
    X2.append(x/100)
    Y1.append(y1)
    Y2.append(-y1)
for a in X1:
    X.append(a)
for a in Y1:
    Y.append(a)
Y2.reverse()
X2.reverse()
for a in X2:
    X.append(a)
for a in Y2:
    Y.append(a)

py.plot([-10, 10], [0, 0], label=" X axis ")
py.plot([0, 0], [-10, 10], label=" Y axis ")
py.plot(X, Y, "g--", label="Circle")
py.legend()
py.show()
