def binarytoint(num):
    temp = 0
    decimal = len(num)
    for i in range(0, len(str(num))):
        digit = temp % 10
        decimal = decimal + digit*(2**i)
        temp//=10

num = str(input("Enter binary number: "))
print(binarytoint(num))
