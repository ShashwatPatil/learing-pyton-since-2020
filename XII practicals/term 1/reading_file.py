
with open("how are you.txt", "w+") as f:
    f.write("how are you ?\n")
    f.write("I am fine.\n")
    f.write("why are you asking ?\n")
    f.write("NOTHING......\n")

with open("how are you.txt", "r+") as f:
    a = f.readlines()
    for x in a:
        b = x.split()
        string = ''
        for z in b:
            string += '#'
            string += z
        print(string)
