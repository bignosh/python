def myFunction(n):
    for i in range(0, n+1):
        print("First loop")
myFunction(10)

# myFunction1 has number of iterations as n, so when n = 10, number of times first loop is printed is 0 to 10 + 1. 
# The time complexity is therefore n

def myFunction2(n2):
    j = 1
    while(j<=n2+1):
        print("Second loop", j)
        j = j*2
myFunction2(10)

# myFunction2 has number of iterations as 

def myFunction3(n3):
    for i in range(0, 100):
        print("Third loop")
myFunction3(10)
