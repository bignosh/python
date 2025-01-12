def computepower(x, y):

    result = 1
    
    while y > 0:
        if y % 2 == 0:
            x = x * x
            y >>= 1
        
        else:
            result = result * x
            y = y - 1
    return result

x = int(input("Enter a value for x in x ^ y: "))
y = int(input("Enter a value for y in x ^ y: "))
print("x^y = ", computepower(x, y))
