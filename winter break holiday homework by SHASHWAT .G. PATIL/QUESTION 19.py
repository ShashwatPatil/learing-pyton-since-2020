string = str(input("Enter a string :"))
element = str(input("enter the element to calculate its frequency in the string entered by you:"))
print("frequency = number of occurrence of that element in the data")
freq = 0
for a in string:
    if a == element:
        freq += 1
    else:
        continue
print(freq, "is the frequency of ", "'", element, "'")
