
with open("how are you.txt", "w+") as f:
    f.write("how are you ?\n")
    f.write("I am fine.\n")
    f.write("why are you asking ?\n")
    f.write("NOTHING......\n")

with open("how are you.txt", "r+") as f:
    a = f.readlines()
    _a = []
    _nota = []
    for x in a:
        for b in x:
            if b == "a":
                _a.append(b)
            else:
                _nota.append(b)

with open("how are you(without a).txt", "w+") as f:
    for x in _nota:
        f.write(x)
with open("how are you(without a).txt", "r") as f:
    data = f.read()
    print(data)
