def ask_for_next_calculation():
    while True:
        try:
            user_input = input("Do you want to perform another calculation? (yes/no): ").lower()
            if user_input in ['yes', 'no']:
                return user_input == 'yes'
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except Exception as e:
            print(f"An error occurred: {e}")