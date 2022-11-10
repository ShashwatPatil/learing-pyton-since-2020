print("Enter only numbers ")
try:
    from decimal import *
    a = float(input("enter numerator : "))
    b = float(input("enter denominator  : "))
    c = int(input("enter resolution of decimal places : "))
    if a == 0:
        print(0)
    else:
        getcontext().prec = int(c)
        print(Decimal(a) / Decimal(b))
except ValueError:
    print("enter number only. ")
except MemoryError:
    print("over limit.")
except OverflowError:
    print("over limit.")
except DivisionByZero:
    print("cannot divide by zero")
