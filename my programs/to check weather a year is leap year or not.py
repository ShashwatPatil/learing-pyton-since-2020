# to check weather a year is leap year or not


year = int(input("enter year you want to check :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is NOT a leap year.")
