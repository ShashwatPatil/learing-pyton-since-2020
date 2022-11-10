
import pickle

print("first make a file with roll no nad name!")

stu = int(input("Enter the number of students in the class :"))

Data = []
temp = []

for num in range(stu):
    name = input("Enter the name of student :")
    roll_no = int(input("Enter the roll no of student :"))
    temp = [roll_no, name]
    Data.append(temp)

with open("Student_info.bin", 'wb+') as f:
    pickle.dump(Data, f)
    print("Data successfully added to the file.!")

ser = int(input("Enter the roll no to be searched :"))
lst = []
with open("Student_info.bin", 'rb+') as file:
    Dats_new = pickle.load(file)
    for a in Dats_new:
        lst.append(a)
    for a in Dats_new:
        if a[0] == ser:
            print(a[1], "is the student with roll no", ser)
        elif a in lst:
            pass
        else:
            print("roll no does not exist")
