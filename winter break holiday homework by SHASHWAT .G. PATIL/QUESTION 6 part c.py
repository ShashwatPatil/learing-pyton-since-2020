
num = str(input("Enter a number:"))
try:
    int(num)
    num_01 = num[::-1]
    if num == num_01:
        print(num, "is an palindrome number.")
    else:
        print(num, "is NOT an palindrome number.")
except ValueError:
    print("please enter only an integer!!!")
