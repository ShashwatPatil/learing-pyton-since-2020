
with open("how are you.txt", "w+") as f:
    f.write("how are you ?\n")
    f.write("I am fine.\n")
    f.write("why are you asking ?\n")
    f.write("NOTHING......\n")
    print(f.tell())
    print(f.seek(0))
    print("this is the data of the file.")
    data = f.read()
    print(data)
