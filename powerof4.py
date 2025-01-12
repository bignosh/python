def powerof4(num):

    count = 0

    if (num & (~(num & (num - 1)))):

        while num > 1:
            num >>= 1
            count += 1

        if count % 2 == 0:
            return True
        else:
            return False
        
num = int(input("Enter a number to see if it's a power of 4: "))
if powerof4(num):
    print(f"{num} is a power of 4")
else:
    print(f"{num} is not a power of 4")
