import math

class Calculator:

    def add(self, x, y):
        try:
            return x + y
        except Exception as e:
            return f"Error: {e}"

    def subtract(self, x, y):
        try:
            return x - y
        except Exception as e:
            return f"Error: {e}"

    def multiply(self, x, y):
        try:
            return x * y
        except Exception as e:
            return f"Error: {e}"

    def divide(self, x, y):
        try:
            if y == 0:
                raise ValueError("Division by zero is undefined.")
            return x / y
        except Exception as e:
            return f"Error: {e}"

    def exponentiate(self, x, y):
        try:
            return x ** y
        except Exception as e:
            return f"Error: {e}"

    def sqrt(self, x):
        try:
            if x < 0:
                raise ValueError("Square root of a negative number is undefined.")
            return math.sqrt(x)
        except Exception as e:
            return f"Error: {e}"

    def remainder(self, x, y):
        try:
            if y == 0:
                raise ValueError("Division by zero is undefined.")
            return x % y
        except Exception as e:
            return f"Error: {e}"
