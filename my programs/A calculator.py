# A SIMPLE CALCULATOR
loop = True
while loop:
    print('''
    **********SELECT WHAT YOU WANT TO CALCULATE**************
    *    you have to enter the sr.no of what you want to do *
    * 1          greatest numbers in four numbers           *
    * 2          greatest numbers in three numbers          * 
    * 3          volume of cuboid                           *
    * 4          division of two numbers                    *
    * 5          TSA of cylinder                            *
    * 6          TSA of right circular cone                 *
    * 7          volume of right circular cone              *
    * 8          CSA of cylinder                            *
    * 9          greater of two numbers                     *
    * 10         area of rectangle                          *
    * 11         CSA of right circular cone                 *
    * 12         volume of cylinder                         *
    * 13         area of triangle                           *
    * 14         sum of two terms                           *
    * 15         product of two num                         *
    * 16         circumference of circle                    *
    * 17         area of circle                             *
    * 18         TSA of sphere                              *
    * 19         volume of cube                             *
    * 20         volume of sphere                           *
    * 21         division of two num                        *
    *********************************************************             
    ''')

    s = int(input("enter the no as per your will and what you want to do :"))

    if s == 1:
        a = float(input("enter first number:"))
        b = float(input("enter second number:"))
        c = float(input("enter third number:"))
        d = float(input("enter fourth number:"))
        if a > b and a > c and a > d:
            print("greatest no is:", a)
        elif b > c and b > d:
            print("greatest no is:", b)
        elif c > d:
            print("greatest no is:", c)
        elif d > c:
            print("greatest no is:", d)
        else:
            print("Either any two values or all the four values are equal")

    elif s == 2:
        a = float(input("enter first no :"))
        b = float(input("enter second no :"))
        c = float(input("enter third no :"))
        if a > b:
            if a > c:
                print("the greatest no is:", a)
            else:
                print("the greatest no is:", c)
        else:
            if b > c:
                print("the greatest no is:", b)
            else:
                print("the greatest no is:", c)

    elif s == 3:
        L = float(input("enter the length of rectangle in cm: "))
        b = float(input("enter the breadth of rectangle in cm:"))
        h = float(input("enter the height of rectangle in cm:"))
        print("the volume of rectangle is in cm cube is :", L*b*h)

    elif s == 4:
        # division of two num
        print("num1/num2 is the format of program")
        a = float(input("enter the value of num 1:"))
        b = float(input("enter the value of num 2:"))
        print("your answer is :", a/b)

    elif s == 5:
        # TSA of cylinder
        h = float(input("enter the value of height of cylinder:"))
        r = float(input("enter the value of radius of cylinder:"))
        print("TSA of cylinder is :", 2*22/7*r*h+2*22/7*r**2)

    elif s == 6:
        # TSA of a right circular cone
        r = float(input("enter the radius of cone:"))
        L = float(input("enter the length of cone:"))
        print("TSA of right circular cone is :", 22/7*r*L+22/7*r**2)

    elif s == 7:
        # volume of a right circular cone
        r = float(input("enter the radius of cone:"))
        h = float(input("enter the height of cone:"))
        print("CSA of right circular cone is :", 1/3*22/7*h*r**2)

    elif s == 8:
        # CSA of cylinder
        h = float(input("enter the value of height of cylinder:"))
        r = float(input("enter the value of radius of cylinder:"))
        print("CSA of cylinder is :", 2*22/7*r*h)
    elif s == 9:
        # Greatest of two numbers
        a = float(input("enter num 1 :"))
        b = float(input("enter num 2 :"))

        if a > b:
            print("num 1 is greater .")
        else:
            print("num 2 is greater .")

    elif s == 10:
        L = float(input("enter the length of rectangle in cm:"))
        b = float(input("enter the breadth of rectangle in cm:"))
        print("the area of rectangle is in cm square is :", L*b)

    elif s == 11:
        # CSA of a right circular cone
        r = float(input("enter the radius of cone:"))
        L = float(input("enter the length of cone:"))
        print("CSA of right circular cone is :", 22/7*r*L)

    elif s == 12:
        # volume of cylinder
        h = float(input("enter the height of cylinder:"))
        r = float(input("enter the radius of cylinder:"))
        print("the volume of sphere is :", 22/7*h*r**2)

    elif s == 13:
        # area of triangle
        b = float(input("enter the base of triangle :"))
        h = float(input("enter the height of triangle :"))
        print("the area of triangle is:", 1/2*b*h)

    elif s == 14:
        # sum of two terms
        num1 = float(input("Enter the value of no. 1 here:"))
        num2 = float(input("Enter the value of no. 2 here:"))
        print("the sum is :", num1+num2)

    elif s == 15:
        # Product of two integers
        a = float(input("enter num 1 :"))
        b = float(input("enter num 2 :"))
        print("product is :", a*b)

    elif s == 16:
        # Circumference of circle
        r = float(input("enter the radius of circle :"))
        print("the circumference is :", 2*22/7*r)

    elif s == 17:
        # area of circle
        r = float(input("enter the radius of circle:"))
        print("the area of circle is :", 22/7*r**2)

    elif s == 18:
        # TSA of sphere
        r = float(input("enter the radius of sphere:"))
        print("the TSA of sphere is:", 4*22/7*r**2)

    elif s == 19:
        # volume of cube
        L = float(input("enter the side of cube :"))
        print("volume of cube:", L*L*L)

    elif s == 20:
        # volume of sphere
        r = float(input("enter the radius of sphere:"))
        print("volume of sphere", 4/3*22/7*r**3)
    elif s == 21:
        a = float(input("enter your numerator :"))
        b = float(input("enter your denominator :"))
        if b != 0:
            print("the ans is :", a/b)
        else:
            print("cannot divide by zero or the ans is infinity")
    else:
        print("wrong input")
    q = input('do you want to use it again[Y/N]')
    if q == 'Y' or q == 'y':
        loop = True
    else:
        loop = False
