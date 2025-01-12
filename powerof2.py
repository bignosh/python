def powerof2(number):

    if number == 0:
        return 0
    if ((number & (~(number - 1))) == number):
        return 1
    return 0

number = int(input("Enter a number to see if it's a power of two: "))

if powerof2(number):
    print(f"{number} is a power of 2")
else:
    print(f"{number} is not a power of 2")
