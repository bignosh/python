import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
studentsdetails = [('James', 5, 48.5), ('Nail', 6, 52.4), ('Paul', 5, 42.10), ('Oliver', 6, 41.6)]
students = np.array(studentsdetails, dtype = data_type)
print("Original array")
print(students)
print("Sort by height order")
print(np.sort(students, order='height'))

a = np.array([5, 10, 15])
print("First array: ")
print(a)
print("\n")

b = np.array([10, 10, 10])
print("Second array: ")
print(b)
print("\n")

choice = input("Choose an option: a(+)/b(-)/c(*)/d(/): ")
if choice == 'a':
    print("Add the 2 arrays: ")
    print(np.add(a, b))
    print("\n")
elif choice == 'b':
    print("Subtract the 2 arrays: ")
    print(np.subtract(a, b))
    print("\n")
elif choice == 'c':
    print("Multiply the 2 arrays: ")
    print(np.multiply(a, b))
    print("\n")
else:
    print("Divide the 2 arrays: ")
    print(np.divide(a, b))
    print("\n")
