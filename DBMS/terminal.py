
from functions import *

W = """
*********************************************************************
*     1 Show tables                                                 *
*     2 Show data                                                   *
*     3 Create new account                                          *
*     4 Search your data                                            *
*     5 Update existing account                                     *
*     6 Delete existing account                                     *
*     7 Exit                                                        *
*********************************************************************
"""
T = True

while T:
    print(W)
    chc = int(input("Enter your choice :"))
    if chc == 1:
        print("Showing you All tables .")
        show()
    elif chc == 2:
        print("Showing data in tables .")
        data()
    elif chc == 3:
        print("Enter your data to make your account .")
        add()
    elif chc == 4:
        print("Search your data .")
        search()
    elif chc == 5:
        print("Update your existing account")
        update()
    elif chc == 6:
        print("Delete existing account")
        delete()
    elif chc == 7:
        print("Exited")
        T = False
    else:
        loop = input("Do you want to continue [Y or y] :")
        if loop == 'y' or loop == 'Y':
            T = False
        else:
            pass
