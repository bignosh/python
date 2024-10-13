def myFunction1(n):
    if n>0:
        return
    for i in range(0, n+1):
        print("Something")
    myFunction1(n/2)
    myFunction1(n/3)
print(myFunction1(5))
#the number of iterations myFunction1 has is n. If n = 5, myFunction = 6+1/2, 3/3
#therefore the time complexity of myFunction1 is in order of T(n+1)


def myFunction2(n):
    if n<=1:
        return
    print("Something else")
    myFunction2(n-1)
print(myFunction2(5))

#
