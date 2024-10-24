num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

valid_operations = ['+', '-', '*', '/']
operation = input("Enter the operation (+, -, *, /): ")

while operation not in valid_operations:
    print("Invalid operator. Please enter a valid operator (+, -, *, /).")
    operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    print("The result is " + str(num1 + num2))
elif operation == '-':
    print("The result is " + str(num1 - num2))
elif operation == '*':
    print("The result is " + str(num1 * num2))
elif operation == '/':
    print("The result is " + str(num1 / num2))
