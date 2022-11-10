
Master = []
with open(r"E:\practical\file making\PAKfile.txt", "r") as f:
    sot = " "
    while sot:
        L = []
        f_read = str(f.readline())
        for a in f_read:
            L.append(a)
        Master += L
        sot = f_read

with open("New_content.txt", "w+") as P:
    for x in Master:
        P.write(x)
    print(P.tell(), "bytes")
