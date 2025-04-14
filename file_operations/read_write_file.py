filename = "example.txt"
with open(filename, 'w') as f:
    f.write("This is a sample file.\nLine 2.")

with open(filename, 'r') as f:
    content = f.read()
    print("File content:\n", content)