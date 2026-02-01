from colorama import Fore, Style

# We wrap the whole logic in a 'while True' loop
while True:
    print("\n--- New Calculation ---")
    
    # 1. Ask for operation first (so we can check if they want to quit)
    operation = input("Enter operator (+, -, *, /, %) or 'q' to quit: ")

    # 2. Check for exit
    if operation.lower() == 'q':
        print("Goodbye!")
        break  # This stops the loop

    # 3. If they didn't quit, ask for numbers
    # We use try/except to catch if they type text instead of numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(Fore.RED + "Error: Please enter valid numbers!" + Style.RESET_ALL)
        continue  # Skip to the next loop iteration

    # 4. Perform Math
    if operation == "+":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print(Fore.RED + "Error: Division by Zero!" + Style.RESET_ALL)
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2:.2f}")
    elif operation == "%":
        if num2 == 0:
            print(Fore.RED + "Error: Division by Zero!" + Style.RESET_ALL)
        else:
            print(f"Result: {num1} % {num2} = {num1 % num2}")
    else:
        print(Fore.RED + "Error: Invalid Operation!" + Style.RESET_ALL)
