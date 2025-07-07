# Simple Hello World and Sum Program

def add(a, b):
    return a + b

print("Hello, Dev!")  # Greeting

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call add function
result = add(num1, num2)

print(f"The sum of {num1} and {num2} is: {result}")
