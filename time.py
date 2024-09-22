def fun1(n):
    sum = n*(n+1)/2
    print(sum)
fun1(40000)

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum+i
    print(sum)
fun2(40000)

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum = sum+1
    print(sum)
fun3(40000)

#algorithm1 has number of iterations as 1, when value of n = 4, sum = 4*5/2.

#Since it has only one step, time complexity is in the order constant

#algorithm2 has number of iterations as 4 when value of n = 4, sum = 1+2+3+4

#since it has 4 steps, the order of the complexity is in n

#algorithm3 has number of iterations as 10, when value of n = 4, sum = 1+(1+1)+(1+1+1)+(1+1+1+1)

#since it has 10 steps, the order of the complexity is in n^2
