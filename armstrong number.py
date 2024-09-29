def armstrong(n):
    temp = n
    num = 0
    if (n>99) and (n<1000):
        while temp > 0:
            digit = temp % 10
            num = digit**3 + num
            temp = temp // 10
    if num == n:
        print("armstrong number")
    else:
        print("not armstrong number")
armstrong(370)
