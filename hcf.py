largest = int(input("Enter largest number: "))
smallest = int(input("Enter smallest number: "))

l = largest
s = smallest

while(smallest):
    numstore = smallest
    smallest = largest % smallest
    largest = numstore

print(f"The HCF of {s} and {l} is {largest}")

lcm = (s * l) / largest
print(lcm)
