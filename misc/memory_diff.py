list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("Address of list1:", id(list1))
print("Address of list2:", id(list2))
print("Address of list3:", id(list3))

print("\nIs list1 the same object as list2?", list1 is list2)
print("Is list1 the same object as list3?", list1 is list3)