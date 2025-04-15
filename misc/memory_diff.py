list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("Address of list1:", id(list1))
print("Address of list2:", id(list2))
print("Address of list3:", id(list3))

print("\nIs list1 the same object as list2?", list1 is list2)
print("Is list1 the same object as list3?", list1 is list3)

# Integer caching
value1 = 5
value2 = 5
value3 = value1

print("Address of value1:", id(value1))
print("Address of value2:", id(value2))
print("Address of value3:", id(value3))

print("\nIs value1 the same object as value2?", value1 is value2)
print("Is value1 the same object as value3?", value1 is value3)

