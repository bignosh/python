a = 7
b = 3
def swapwithop(a, b):
    
    a = a + b
    b = a - b
    a = a - b
    print("swapped: a = ", a, "b = ", b)

def swapwithxor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("Swapped: a = ", a, "b = ", b)

def swapwithbool(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("Swapped: a = ", a, "b = ", b)

swapwithop(a, b)
swapwithxor(a, b)
swapwithbool(a, b)
