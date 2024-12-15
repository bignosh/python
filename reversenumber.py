def reversebinary():
    num = int(input("Enter a number: "))
    binarynum = bin(num)[2:]
    reversedbin = binarynum[::-1]
    reversedint = int(reversedbin, 2)
    
    print("Your number is", num, ", and in binary form is", binarynum)
    print("Your number reversed is", reversedint, ", and as a binary number", reversedbin)

reversebinary()
