settings = {
    "decimal_places": 2,      # За замовчуванням кількість знаків після коми
    "auto_memory_save": False,  # Автоматичне збереження результатів в пам'ять
    "auto_memory_clear": False
}

def set_decimal_places():
    try:
        decimal_places = int(input("Enter the number of decimal places to display (0-10): "))
        if 0 <= decimal_places <= 10:
            settings["decimal_places"] = decimal_places
            print(f"Decimal places set to {decimal_places}.")
        else:
            print("Please enter a number between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def toggle_auto_memory_save():
    settings["auto_memory_save"] = not settings["auto_memory_save"]
    status = "enabled" if settings["auto_memory_save"] else "disabled"
    print(f"Auto Memory Save is now {status}.")

def toggle_auto_memory_clear():
    settings["auto_memory_clear"] = not settings["auto_memory_clear"]
    status = "enabled" if settings["auto_memory_clear"] else "disabled"
    print(f"Auto Memory Clear is now {status}.")

def format_result(result):
    return f"{result:.{settings['decimal_places']}f}"