import pickle
with open("how are you.txt", "r") as f:
    data = f.readlines()
    with open("appended file.bin", "wb+") as app_file:
        Lst = []
        for a in data:
            Lst.append(a)
        pickle.dump(Lst, app_file)

        app_file.seek(0)
        obj = pickle.load(app_file)
        print(obj)
