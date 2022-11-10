def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


arry = list(input("enter the elements of list"))
a = input("enter the element to be searched: ")
arry.sort()
result = binary_search(arry, 0, len(arry) - 1, a)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
