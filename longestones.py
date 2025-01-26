def ones(binnum):
    count = 0
    while binnum != 0:
        binnum = binnum & (binnum << 1)
        count = count + 1
    return count

num = int(input("Enter a number: "))
binnum = bin(num)[2:]
print("The longest amount of ones is ", ones(binnum))
