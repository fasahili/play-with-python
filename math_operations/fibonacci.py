def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter the number of Fibonacci terms: "))
print(f"Fibonacci sequence: {fibonacci(n)}")
