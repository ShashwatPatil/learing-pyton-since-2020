### PRACTICAL FOR XI CS - 2020-21 #
#10 Count and display the number of vowels, consonants, uppercase,
# lower case characters in string

str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0
capitals=0

for ch in str1:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
       or ch== 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

    if(ch>='A' and ch<='Z'):
       capital+=1
print("Total Number of Vowels= ", vowels)
print("Total Number of Consonants = ", consonants)
print("Total Number of Capital etter = ", capitals)
