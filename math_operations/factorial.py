def factorial(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")