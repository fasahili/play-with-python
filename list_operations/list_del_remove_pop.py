items = [10, 20, 30, 40, 50]

del items[1] #[10,30,40,50]
items.remove(30) #[10,40,50]
popped_item = items.pop(1) #[10,50]

print("Final list:", items)
print("Popped item:", popped_item)