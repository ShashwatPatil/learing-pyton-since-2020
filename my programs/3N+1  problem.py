import csv

with open("3n+1 problem.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["number", "iterations", "working"])

n = 1
while n < 10:
    i = 0
    All = [n]
    temp = []
    k = n
    while k != 1:
        temp.append(k)
        if k % 2 == 1:
            k = (3 * k) + 1
        elif k % 2 == 0:
            k = k / 2
        else:
            pass
        i += 1
    i += 1
    temp.append(1.0)
    All.append(i)
    All.append(temp)
    with open("3n+1 problem.csv", "a", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(All)
    n += 1
