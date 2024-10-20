number = int(input("Enter number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original == reverse:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")
