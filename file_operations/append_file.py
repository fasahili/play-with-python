filename = "example.txt"
with open(filename, 'a') as f:
    f.write("\nAppended line.")

with open(filename, 'r') as f:
    print("Updated file content:\n", f.read())
