perform_another_calculation = 'yes'

while perform_another_calculation == 'yes':
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

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
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("The result is " + str(num1 / num2))

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except OverflowError:
        print("Error: The number you entered is too large.")

    perform_another_calculation = input("Do you want to perform another calculation? (yes/no): ")

