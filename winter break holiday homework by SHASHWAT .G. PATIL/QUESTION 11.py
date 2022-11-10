string = str(input("Enter a string."))
ori_string = string.lower()
rev_string = ori_string[::-1]
if ori_string == rev_string:
    print(ori_string, "is a palindrome.")
else:
    print(ori_string, "is NOT a palindrome.")
