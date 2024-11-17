def oddoreven(n):
    if (n^1 == n+1):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

n = int(input("Enter a number: "))
oddoreven(n)
