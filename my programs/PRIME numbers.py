list_prime = [2]
list_01 = []
num = 2
print(2)
while True:
    b = str(num)[-1]
    if num % 2 == 0:
        num += 1
    elif str(num)[-1] == 5:
        num += 1
    else:
        for a in list_prime:
            if num % a == 0:
                list_01.append(num)
                if len(list_01) != 0:
                    break
        if len(list_01) == 0:
            list_prime.append(num)
            print(num)
        num += 1
    list_01.clear()
