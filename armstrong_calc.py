number = int(input("Enter a number: "))

alldigits = len(str(number))

temp = number
result = 0

while temp > 0:
    digit = temp % 10
    result += digit ** alldigits
    temp = temp // 10

if number == result:
    print("It's an armstrong number")
else:
    print("It isn't an armstrong number")
