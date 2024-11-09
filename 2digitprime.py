from math import sqrt

num = int(input("Enter number to check if it is prime: "))
print("\n")

if num > 1:
    if len(str(num)) == 2:
        for i in range (2, int(sqrt(num))+1):
            if (num % i) == 0:
                print(f"{num} is not prime number")
                break
            else:
                print(f"{num} is prime")
    else:
        print("Enter number that is only 2 digits")
elif num == 1:
    print("1 cannot be prime")
else:
    print(f"{num} should be a positive integer")
