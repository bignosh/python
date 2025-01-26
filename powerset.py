import math
def powerset(set, setsize):
    Powerset = (int) (math.pow(2, setsize))
    outer = 0
    inner = 0

    for outer in range(0, Powerset):
        for inner in range(0, setsize):
            if ((outer & (1 << inner)) > 0):
                print(set[inner], end = "")
        print("")

setsize = int(input("Enter array size: "))
set = []
for i in range(0, setsize):
    n = int(input("Enter an element: "))
    set.append(n)

print(powerset(set, setsize))
