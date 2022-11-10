
import random as r
import matplotlib.pyplot as plt
import math as m
print("enter the values of two equations in the standard form ONLY !!!! ")
# if a1 and a2 and b1 and b2 and c1 and c2.isnumeric() is True:
X1 = []
Y1 = []
X2 = []
Y2 = []
eq_1 = []
eq_2 = []
a_1 = []
b_1 = []
try:
    a1 = float(input("enter the value of coefficient x of first equation : "))
    b1 = float(input("enter the value of coefficient y of first equation : "))
    c1 = float(input("enter the value of constant of first equation : "))
    a2 = float(input("enter the value of coefficient x of second equation : "))
    b2 = float(input("enter the value of coefficient y of second equation : "))
    c2 = float(input("enter the value of constant of second equation : "))
    A1 = a1
    B1 = b1
    C1 = c1
    A2 = a2
    B2 = b2
    C2 = c2
    if a1 == a2 == 0:
        print("value of Y has to be 0. as both the coefficient of X are 0(Zero) ")
    elif b1 == b2 == 0:
        print("value of X has to be 0. as both the coefficient of Y are 0(Zero) ")
    else:
        try:
            if a2 == 0 or b2 == 0:
                if a2 == 0:
                    Y_00 = float(c2) / float(b2)
                    print("the value of Y is : ", Y_00)
                    X_00 = (float(c1) - (float(b1) * Y_00)) / float(a1)
                    print("the value of X is : ", X_00)
                elif b2 == 0:
                    X_00 = float(c2) / float(a2)
                    print("the value of X is : ", X_00)
                    Y_00 = (float(c1) - (float(a1) * X_00)) / float(b1)
                    print("the value of Y is : ", Y_00)
                else:
                    print("ERROR ")
            elif a1 == 0 or b1 == 0:
                if a1 == 0:
                    Y_00 = float(c1) / float(b1)
                    print("the value of Y is : ", Y_00)
                    X_00 = (float(c2) - (float(b2) * Y_00)) / float(a2)
                    print("the value of X is : ", X_00)
                elif b1 == 0:
                    X_00 = float(c1) / float(a1)
                    print("the value of X is : ", X_00)
                    Y_00 = (float(c2) - (float(a2) * X_00)) / float(b2)
                    print("the value of Y is : ", Y_00)
                else:
                    print("error ")
            else:
                if float(a1) / float(a2) == float(b1) / float(b2) == float(c1) / float(c2):
                    print("X and Y has infinite solutions")
                    for_x = []
                    for_y = []
                    for x in range(10):
                        if x % 2 == 0:
                            a = r.randint(10, 100)
                            b = r.randint(-100, -10)
                            for_x.append(a)
                            for_x.append(b)
                        else:
                            a = r.randint(10, 100)
                            b = r.randint(-100, -10)
                            for_y.append(a)
                            for_y.append(b)
                    for q in for_x:
                        a_1.append(q)
                        y_ans = (c1 - a1 * q) / b1
                        eq_2.append(y_ans)
                    for g in for_y:
                        b_1.append(g)
                        x_ans = (c2 - b2 * g) / a2
                        eq_1.append(x_ans)
                    plt.plot(a_1, eq_2)
                    plt.plot(b_1, eq_1)
                    plt.show()
                elif float(a1) / float(a2) == float(b1) / float(b2) != float(c1) / float(c2):
                    print("X and Y has NO solutions")
                    for_x = []
                    for_y = []
                    for x in range(10):
                        if x % 2 == 0:
                            a = r.randint(10, 100)
                            b = r.randint(-100, -10)
                            for_x.append(a)
                            for_x.append(b)
                        else:
                            a = r.randint(10, 100)
                            b = r.randint(-100, -10)
                            for_y.append(a)
                            for_y.append(b)
                    for q in for_x:
                        a_1.append(q)
                        y_ans = (c1 - a1 * q) / b1
                        eq_2.append(y_ans)
                    for g in for_y:
                        b_1.append(g)
                        x_ans = (c2 - b2 * g) / a2
                        eq_1.append(x_ans)
                    plt.plot(a_1, eq_2)
                    plt.plot(b_1, eq_1)
                    plt.show()
                else:
                    A_00 = float(float(a2) * float(c1) - float(c2) * float(a1))
                    B_00 = float((float(a2) * float(b1) - float(a1) * float(b2)))
                    Y_00 = float(A_00 / B_00)
                    print("the value of Y is : ", Y_00)
                    C_00 = Y_00 * float(b1)
                    X_00 = float(float(c1) - C_00) / float(a1)
                    print("the value of X is : ", X_00)
                    why = m.floor(X_00)
                    how = m.floor(Y_00)
                    for_x = []
                    for_y = []
                    for x in range(1):
                        if True:
                            a = r.randint(why, how + 1000)
                            b = r.randint(how - 1000, how)
                            for_x.append(a)
                            for_x.append(b)
                        if True:
                            a = r.randint(how, why + 1000)
                            b = r.randint(why - 1000, how)
                            for_y.append(a)
                            for_y.append(b)
                    for q in for_x:
                        a_1.append(q)
                        y_ans = (c1 - a1 * q) / b1
                        eq_2.append(y_ans)
                    for g in for_y:
                        b_1.append(g)
                        x_ans = (c2 - b2 * g) / a2
                        eq_1.append(x_ans)
                    eq_2.append(Y_00)
                    eq_1.append(Y_00)
                    b_1.append(X_00)
                    a_1.append(X_00)
                    plt.plot(a_1, eq_2)
                    plt.plot(b_1, eq_1)
                    plt.show()
        finally:
            print('''THANK YOU FOR USING THIS !!!
                            - BY SHASHWAT PATIL''')
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("Zero Division Error occurred somewhere ")
