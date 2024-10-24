perform_another_calculation = 'yes'

memory = 0
current_result = 0

while perform_another_calculation == 'yes':
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        valid_operations = ['+', '-', '*', '/', '^', '%', '?']
        operation = input("Enter the operation (+, -, *, /, ^, %, ?): ")

        while operation not in valid_operations:
            print("Invalid operator. Please enter a valid operator (+, -, *, /, ^, %, ?).")
            operation = input("Enter the operation (+, -, *, /, ^, %, ?): ")

        if operation == '+':
            current_result = num1 + num2
            print("The result is " + str(current_result))
        elif operation == '-':
            current_result = num1 - num2
            print("The result is " + str(current_result))
        elif operation == '*':
            current_result = num1 * num2
            print("The result is " + str(current_result))
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                current_result = num1 / num2
                print("The result is " + str(current_result))
        elif operation == '^':
            current_result = num1 ** num2
            print("The result is " + str(current_result))
        elif operation == '%':
            current_result = num1 % num2
            print("The result is " + str(current_result))
        elif operation == '?':  # Квадратний корінь
            if num1 < 0:
                print("Error: Square root is only defined for non-negative numbers.")
                continue
            else:
                current_result = num1 ** 0.5
                print("The result is " + str(current_result))

        # Операції пам'яті
        memory_operation = input("Enter memory operation (c, mc, m+, m-, mr, ms): ")

        if memory_operation == 'c':
            current_result = 0
            print("Current result cleared.")
        elif memory_operation == 'mc':
            memory = 0
            print("Memory cleared.")
        elif memory_operation == 'm+':
            memory += current_result
            print("Memory updated: " + str(memory))
        elif memory_operation == 'm-':
            memory -= current_result
            print("Memory updated: " + str(memory))
        elif memory_operation == 'mr':
            print("Memory recall: " + str(memory))
        elif memory_operation == 'ms':
            memory = current_result
            print("Memory stored: " + str(memory))

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except OverflowError:
        print("Error: The number you entered is too large.")

    perform_another_calculation = input("Do you want to perform another calculation? (yes/no): ")
