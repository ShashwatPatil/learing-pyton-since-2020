
def vowel(s):
    v = 0
    z = list("aeiouAEIOU")

    for x in s:
        if x in z:
            v += 1
        else:
            pass
    return v


p = input("enter a string: ")
c = vowel(p)
print(c, "are the number of vowels")
