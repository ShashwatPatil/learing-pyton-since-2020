
import numpy as np
import Matrix_box_info

l0, l1, l2, l3, l4, l5, l6, l7, l8 = Matrix_box_info.all_list()
L_all = [l0, l1, l2, l3, l4, l5, l6, l7, l8]
temp = list(map(int, input().split()))
matrix = np.array(temp).reshape(9, 9)

print(matrix)
M_list = []

for a in range(9):
    for b in range(9):
        t = (a, b)
        M_list.append(t)

A = 1

while A != 0:

    for p in M_list:
        A = 0
        B = 0
        if matrix[p] == 0:
            x, y = p[0], p[1]
            list_new = []
            K = []
            M = []
            for i in range(9):
                K.append((x, i))
                M.append((i, y))
            list_new = list_new + K + M
            for m in L_all:
                if p in m:
                    list_new = list_new + m
                    break
                else:
                    pass
            for i in range(1, 10):
                B = 0
                for x in list_new:
                    if i == matrix[x]:
                        B += 1
                if B == 0:
                    A += 1
            B = 0
            if A == 1:
                for i in range(1, 10):
                    B = 0
                    for x in list_new:
                        if i == matrix[x]:
                            B += 1
                    if B == 0:
                        matrix[p] = i
                        print(matrix, "till here solved pls wait")
    A = 0
    for q in M_list:
        if matrix[q] == 0:
            A += 1

print("solved")
print(matrix)
