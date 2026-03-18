try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")
except ValueError as e:
   print("Error: Invalid input. Please enter a valid number.")