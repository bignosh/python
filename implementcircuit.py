a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Your values' output with the logic circuit is: ", (a & b) | ((b | c) & (b & c)))
