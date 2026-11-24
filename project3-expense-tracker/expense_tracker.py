# Project 3 - Personal Expense Tracker with CSV
import csv
import os
from datetime import datetime


folder = os.path.dirname(__file__)
filename = os.path.join(folder, "expenses.csv")


def load_expenses():
    expenses = []
    if not os.path.exists(filename):
        return expenses

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  
        for row in reader:
            if len(row) < 4:
                continue
            try:
                row[3] = float(row[3])
            except ValueError:
                print("Skipping a row with a bad amount:", row)
                continue
            expenses.append(row)
    return expenses


def save_expense(date, category, description, amount):
    is_new = not os.path.exists(filename) or os.path.getsize(filename) == 0

    
    if not is_new:
        with open(filename, "r", newline="") as file:
            text = file.read()
        if not text.endswith("\n"):
            with open(filename, "a", newline="") as file:
                file.write("\r\n")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if is_new:
            writer.writerow(["date", "category", "description", "amount"])
        writer.writerow([date, category, description, amount])




def get_date():
    while True:
        text = input("Enter date (YYYY-MM-DD), or press Enter for today: ").strip()
        if text == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Wrong date format. Example: 2026-11-24")


def get_month():
    while True:
        text = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(text, "%Y-%m")
            return text
        except ValueError:
            print("Wrong month format. Example: 2026-11")


def get_amount(message):
    while True:
        try:
            amount = float(input(message))
        except ValueError:
            print("Please enter a number.")
            continue
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            return round(amount, 2)


def get_text(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("This cannot be empty.")
        else:
            return text




def add_expense():
    print("\n--- Add Expense ---")
    date = get_date()
    category = get_text("Enter category (food, travel, books...): ").lower()
    description = get_text("Enter description: ")
    amount = get_amount("Enter amount: ")

    save_expense(date, category, description, amount)
    print("Expense saved!")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\nNo. | Date | Category | Description | Amount")
    total = 0
    count = 1
    for e in expenses:
        print(count, "|", e[0], "|", e[1], "|", e[2], "|", format(e[3], ".2f"))
        total += e[3]
        count += 1
    print("Total:", round(total, 2))


def view_expenses():
    print("\n--- All Expenses ---")
    show_expenses(load_expenses())


def filter_expenses():
    expenses = load_expenses()
    print("\n--- Filter Expenses ---")
    print("1. By category")
    print("2. By month")
    print("3. By minimum amount")
    choice = input("Enter your choice: ")
    while choice not in ("1", "2", "3"):
        print("Please choose 1, 2 or 3.")
        choice = input("Enter your choice: ")

    found = []
    if choice == "1":
        category = input("Enter category: ").strip().lower()
        for e in expenses:
            if e[1] == category:
                found.append(e)
    elif choice == "2":
        month = get_month()
        for e in expenses:
            if e[0].startswith(month):
                found.append(e)
    else:
        minimum = get_amount("Show expenses of at least: ")
        for e in expenses:
            if e[3] >= minimum:
                found.append(e)

    show_expenses(found)


def category_summary():
    expenses = load_expenses()
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    totals = {}
    counts = {}
    for e in expenses:
        cat = e[1]
        if cat in totals:
            totals[cat] += e[3]
            counts[cat] += 1
        else:
            totals[cat] = e[3]
            counts[cat] = 1

    print("\n--- Category Summary ---")
    grand_total = 0
    top_category = ""
    top_amount = 0
    for cat in totals:
        print(cat, "- items:", counts[cat], "- total:", round(totals[cat], 2))
        grand_total += totals[cat]
        if totals[cat] > top_amount:
            top_amount = totals[cat]
            top_category = cat

    print("Grand total:", round(grand_total, 2))
    print("Highest spending category:", top_category)


# ----- Main menu -----

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter expenses")
        print("4. Category summary")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()