def oddoccurring(arr):

    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []
n = int(input("Enter length of list: "))

while (n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n -= 1

print("The odd occuring number is", oddoccurring(arr))
