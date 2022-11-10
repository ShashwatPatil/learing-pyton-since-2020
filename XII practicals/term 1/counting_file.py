
with open("how are you.txt", "w+") as f:
    f.write("how are you ?\n")
    f.write("I am fine.\n")
    f.write("why are you asking ?\n")
    f.write("NOTHING......\n")

with open("how are you.txt", "r+") as f:
    string = f.read()
    list_all = []
    vowels, consonant, upper, lower = 0, 0, 0, 0
    for a in range(65, 123):
        list_all.append(chr(a))
    list_consonant = list_all
    list_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in list_vowels:
        try:
            list_consonant.remove(i)
        except ValueError:
            pass
    for x in list_vowels:
        for c in string:
            if x == c:
                vowels += 1
    print("there are ", vowels, "vowels in the entered string")
    for y in list_consonant:
        for h in string:
            if h == y:
                consonant += 1
    print("there are ", consonant, "consonant in the entered string")
    for s in string:
        if s.isalpha():
            if s.isupper():
                upper += 1
            elif s.islower():
                lower += 1
        else:
            continue
    print("there are ", upper, "uppercase alphabets in the entered string")
    print("there are ", lower, "lowercase alphabets in the entered string")
