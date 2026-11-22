# Calculator and Unit Converter
# Python internship - Project 1

# conversion factors
factors = {
    "km_to_miles": 0.621371,
    "miles_to_km": 1.609344,
    "kg_to_pounds": 2.20462,
    "pounds_to_kg": 0.453592
}

# value of 1 unit in INR (approximate rates)
rates = {"USD": 85, "EUR": 92, "GBP": 108}


def get_number(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print("Please enter a valid number!")


def calculator():
    print("\n--- Calculator ---")
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    op = input("Enter operation (+, -, *, /): ")
    while op not in ("+", "-", "*", "/"):
        print("Wrong operation, try again.")
        op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Answer:", num1 + num2)
    elif op == "-":
        print("Answer:", num1 - num2)
    elif op == "*":
        print("Answer:", num1 * num2)
    else:
        while num2 == 0:
            print("Cannot divide by zero!")
            num2 = get_number("Enter second number again: ")
        print("Answer:", num1 / num2)


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. km to miles")
    print("2. miles to km")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. kg to pounds")
    print("6. pounds to kg")

    choice = input("Enter choice (1-6): ")
    while choice not in ("1", "2", "3", "4", "5", "6"):
        print("Invalid choice!")
        choice = input("Enter choice (1-6): ")

    value = get_number("Enter the value: ")

    if choice == "1":
        print(value, "km =", round(value * factors["km_to_miles"], 2), "miles")
    elif choice == "2":
        print(value, "miles =", round(value * factors["miles_to_km"], 2), "km")
    elif choice == "3":
        print(value, "C =", round(value * 9 / 5 + 32, 2), "F")
    elif choice == "4":
        print(value, "F =", round((value - 32) * 5 / 9, 2), "C")
    elif choice == "5":
        print(value, "kg =", round(value * factors["kg_to_pounds"], 2), "pounds")
    else:
        print(value, "pounds =", round(value * factors["pounds_to_kg"], 2), "kg")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("Available currencies: USD, EUR, GBP")

    code = input("Enter currency code: ").upper()
    while code not in rates:
        print("Currency not available!")
        code = input("Enter currency code: ").upper()

    print("1. INR to", code)
    print("2.", code, "to INR")
    choice = input("Enter choice (1 or 2): ")
    while choice not in ("1", "2"):
        print("Invalid choice!")
        choice = input("Enter choice (1 or 2): ")

    amount = get_number("Enter amount: ")

    if choice == "1":
        print(amount, "INR =", round(amount / rates[code], 2), code)
    else:
        print(amount, code, "=", round(amount * rates[code], 2), "INR")


def main():
    print("Welcome!")
    while True:
        print("\n--- Main Menu ---")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Quit")

        option = input("Enter your choice: ")

        if option == "1":
            calculator()
        elif option == "2":
            unit_converter()
        elif option == "3":
            currency_converter()
        elif option == "4":
            print("Thank you, bye!")
            break
        else:
            print("Invalid choice, please try again.")


main()