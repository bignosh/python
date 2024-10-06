def prints(n):
    if n<=0:
        return
    print("Something")
    prints(n/2)
    prints(n/2)
# prints(5)

def sum(n2):
    return n2 * (n2+1)/2
# print(sum(5))

def sum1(n2):
    sum = 0
    for i in n2:
        sum = sum + i
    return sum
a = [1, 2, 3, 4, 5]
# print(sum1(a))

def sum2(n):
    if n<=0:
        return 0
    return n + sum2(n-1)
print(sum2(5))
