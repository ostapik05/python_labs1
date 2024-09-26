from Settings.user_settings import settings, set_decimal_places, toggle_auto_memory_save, toggle_auto_memory_clear, format_result
from Functions.memory_functions import memory_save, memory_recall, memory_clear
from Functions.history_functions import log_history, view_history, clear_history
from Classes.Calculator import Calculator
from ConstantsAndVariables.operation_choices import OPERATIONS, VALID_CHOICES

def get_valid_input(prompt, valid_choices):
    while True:
        try:
            user_input = input(prompt)
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    calc = Calculator()
    print("Select operation:")
    for key, operation in OPERATIONS.items():
        print(f"{key}. {operation}")

    while True:
        choice = get_valid_input(f"Enter choice ({'/'.join(VALID_CHOICES)}): ", VALID_CHOICES)

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '6':
                num = get_float_input("Enter number for square root (√): ")
                if num < 0:
                    print("Cannot calculate the square root of a negative number.")
                    continue
                result = calc.sqrt(num)
                formatted_result = format_result(result)
                print(f"√{num} = {formatted_result}")
                log_history(f"√{num}", formatted_result)
            else:
                num1 = get_float_input("Enter first number: ")
                num2 = get_float_input("Enter second number: ")

                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {format_result(result)}")
                    log_history(f"{num1} + {num2}", format_result(result))
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {format_result(result)}")
                    log_history(f"{num1} - {num2}", format_result(result))
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"{num1} * {num2} = {format_result(result)}")
                    log_history(f"{num1} * {num2}", format_result(result))
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                        continue
                    result = calc.divide(num1, num2)
                    print(f"{num1} / {num2} = {format_result(result)}")
                    log_history(f"{num1} / {num2}", format_result(result))
                elif choice == '5':
                    result = calc.exponentiate(num1, num2)
                    print(f"{num1} ^ {num2} = {format_result(result)}")
                    log_history(f"{num1} ^ {num2}", format_result(result))
                elif choice == '7':
                    result = calc.remainder(num1, num2)
                    print(f"{num1} % {num2} = {format_result(result)}")
                    log_history(f"{num1} % {num2}", format_result(result))

            if settings["auto_memory_save"]:
                memory_save(format_result(result))

        elif choice in ['M+', 'MR', 'MC', 'H', 'CH', 'S1', 'S2', 'S3']:
            if choice == 'M+':
                if 'result' in locals():
                    memory_save(format_result(result))
                else:
                    print("No result to save.")
            elif choice == 'MR':
                recalled_value = memory_recall()
                if recalled_value is not None:
                    print(f"Recalled value: {recalled_value}")
                else:
                    print("No value in memory.")
            elif choice == 'MC':
                memory_clear()
                print("Memory cleared.")
            elif choice == 'H':
                view_history()
            elif choice == 'CH':
                clear_history()
                print("History cleared.")
            elif choice == 'S1':
                set_decimal_places()
            elif choice == 'S2':
                toggle_auto_memory_save()
            elif choice == 'S3':
                toggle_auto_memory_clear()
        else:
            print("Invalid input, please select a valid operation.")

        next_calculation = get_valid_input("Do you want to perform another calculation? (yes/no): ", ['yes', 'no'])
        if next_calculation.lower() != 'yes':
            break

    if settings["auto_memory_clear"]:
        memory_clear()