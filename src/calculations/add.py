def add_numbers(num1, num2):
        if num1 is None or num2 is None:
            raise ValueError("Both numbers must be provided.")

        # Check if both inputs are numbers
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            raise TypeError("Both inputs must be numbers.")
        
        result = num1 + num2
        return result