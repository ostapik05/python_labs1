# Налаштування калькулятора
decimal_places = int(input("Enter the number of decimal places for results (default is 2): ") or 2)
auto_save_to_memory = input("Do you want to automatically save the result to memory after each calculation? (yes/no, default is no): ").strip().lower() or 'no'

memory = 0
current_result = 0
history = []

perform_another_calculation = 'yes'

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
        elif operation == '-':
            current_result = num1 - num2
        elif operation == '*':
            current_result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                current_result = num1 / num2
        elif operation == '^':
            current_result = num1 ** num2
        elif operation == '%':
            current_result = num1 % num2
        elif operation == '?':  # Квадратний корінь
            if num1 < 0:
                print("Error: Square root is only defined for non-negative numbers.")
                continue
            else:
                current_result = num1 ** 0.5

        # Записуємо вираз і результат в історію
        expression = f"{num1} {operation} {num2} = {current_result:.{decimal_places}f}"
        history.append(expression)
        print("The result is " + f"{current_result:.{decimal_places}f}")

        memory_operation = input("Enter memory operation (c, mc, m+, m-, mr, ms) or 'history' to view history: ")

        if memory_operation == 'c':
            current_result = 0
            print("Current result cleared.")
        elif memory_operation == 'mc':
            memory = 0
            print("Memory cleared.")
        elif memory_operation == 'm+':
            memory += current_result
            print("Memory updated: " + f"{memory:.{decimal_places}f}")
        elif memory_operation == 'm-':
            memory -= current_result
            print("Memory updated: " + f"{memory:.{decimal_places}f}")
        elif memory_operation == 'mr':
            print("Memory recall: " + f"{memory:.{decimal_places}f}")
        elif memory_operation == 'ms':
            memory = current_result
            print("Memory stored: " + f"{memory:.{decimal_places}f}")
        elif memory_operation == 'history':
            print("Calculation History:")
            for entry in history:
                print(entry)

        if auto_save_to_memory == 'yes':
            memory = current_result
            print("Memory automatically updated with the current result.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except OverflowError:
        print("Error: The number you entered is too large.")

    perform_another_calculation = input("Do you want to perform another calculation? (yes/no): ")
