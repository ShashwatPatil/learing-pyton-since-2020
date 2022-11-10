
import pickle

print("first make a file with roll no nad name!")

stu = int(input("Enter the number of students in the class :"))

Data = []
temp = []

for num in range(stu):
    name = input("Enter the name of student :")
    roll_no = int(input("Enter the roll no of student :"))
    marks = int(input("Enter the marks of student :"))
    temp = [roll_no, name, marks]
    Data.append(temp)

with open("Student_info.bin", 'wb+') as f:
    pickle.dump(Data, f)
    print("Data successfully added to the file.!")

ser = int(input("Enter the roll no to be update marks :"))
mark = int(input("enter updated marks"))
Data_updated = []

with open("Student_info.bin", 'rb+') as file:
    Dats_new = pickle.load(file)
    for a in Dats_new:
        Data_updated.append(a)
    for a in Data_updated:
        if a[0] == ser:
            a[2] = mark
        else:
            pass

with open("Student_info.bin", 'wb+') as f:
    pickle.dump(Data_updated, f)
    print("Data successfully updated to the file.!")
