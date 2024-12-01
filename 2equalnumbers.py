def checkifsamenum(num1, num2):

    if (num1 ^ num2) != 0:
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
checkifsamenum(num1, num2)
