
import pickle
L = []
with open(r"E:\practical\file making\New_content.txt", "r+") as _file:
    for a in _file:
        L.append(a)

with open(r"E:\practical\file making\New_content.bin", "wb+") as Binfile:
    pickle.dump(L, Binfile)

with open(r"E:\practical\file making\New_content.bin", "rb+") as Binfile_0:
    P = pickle.load(Binfile_0)
    print(P)
