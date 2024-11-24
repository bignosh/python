def firstbit(n):

    count = 1

    while(n):

        if (n&1 == 1):

            break

        count += 1

        n >>= 1

    return count

n = int(input("Enter a number: "))
print(firstbit(n))

def zeroesandones(n1):

    zeroes = 0
    ones = 0

    while(n1):

        if(n1&1 == 1):
            ones += 1
        else:
            zeroes += 1

        n1 >>= 1
    
    print(f"there are", zeroes, "zeroes and", ones, "ones")

n1 = int(input("Enter a number: "))
zeroesandones(n1)

def setornot(number, n2):

    if (number & 1<<(n2-1)):
        print("\nSET")
    else:
        print("\nNOT SET")

number = int(input("Enter a number: "))
n2 = int(input("Enter bit number: "))
setornot(number, n2)
