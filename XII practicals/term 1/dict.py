
n = int(input("enter value of n :"))
d = {}

for i in range(n):
    keys = input("enter the keys ")
    values = input("enter the values ")
    d[keys] = values
print(d)


def dict_my(key, value):
    d[key] = value


a = input("enter the key to be updated:")
b = input("enter the value to be updated:")
dict_my(a, b)
print(d, "is the updated dictionary")
