def setofbit(arr1, arr_size):

    set_bit = 0
    x = 0
    y = 0
    xorof2 = arr[0]

    for i in range(1, arr_size):
        xorof2 = xorof2 ^ arr1[i]

    setbit = xorof2 & ~(xorof2 - 1)
    
    for i in range(arr_size):
        
        if arr1[i] & setbit:
            x = x ^ arr1[i]
        else:
            y = y ^ arr1[i]
    
    print("The 2 odd elements are", x, "and", y)

arr = []

arr_size = int(input("Enter array size: "))
for i in range(0, arr_size):
    z = int(input("Enter element: "))
    arr.append(z)
setofbit(arr, arr_size)
