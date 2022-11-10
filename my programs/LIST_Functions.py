# list.extend() # to join to lists together
# list.append() # to add an element\value at the end of list
# list.insert() # to place a element\value in a particular
# list.remove() # to remove certain element\value in the existing list
# list.clear()  # to reset the list --->remove every element of the list
# list.pop()    # to remove the last element\value of the list
# print(list.index(value in the list eg-- a number or value))  # to get the index value of a element in the list
# print(name of the list.count("element\value"))
# name of the list.sort() # to sort the list in alphabetical order or numbers in ascending order
# name of the list.reverse() # to reverse the sorted\unsorted list


list_00 = [-1, 1, 2, 3, 4, 5, 1, 1, 2, 1, 1, 0]
list_00.remove(4)
list_01 = ["tom", "jerry", "spike", "tike", "apple", "spider", "ironman"]
print(list_00)

print(list_00.index(1))

print(list_00.index(3))
list_00.sort()
list_01.sort()

print(list_01)
print(list_00)

list_00.reverse()
list_01.reverse()

print(list_00)
print(list_01)

list_00.pop()
print(list_00)

print(list_00.count(1))

print(list_00.index(1))
list_00.clear()
print(list_00)

exit(list_00)
