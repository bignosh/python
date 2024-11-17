def numofbits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1

    return count

num = int(input("Enter a number: "))
print("Number of bits in your number is ", numofbits(num))
