
import math
import random
import time
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = random.random() * 100
r = math.floor(r)
print('Processing', end='')
for a in list_1:
    print('.', end='')
    time.sleep(0.6)
print()
time.sleep(2)
for a in list_1:
    print(r, "X", a, "=", a*r)
    time.sleep(0.5)
