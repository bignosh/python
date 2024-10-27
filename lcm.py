largest = int(input("Enter largest number: "))
smallest = int(input("Enter smallest number: "))

l = largest
s = smallest

lcm = (s * l) / largest
print(f"The LCM of {smallest} and {largest} is {lcm}")
