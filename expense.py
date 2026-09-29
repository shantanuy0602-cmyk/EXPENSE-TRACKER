from data import save_expense, get_expenses


def add_expense():
    print()
    print("--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount should be greater than 0.")
            return

        save_expense(date, category, amount, note)
        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    expenses = get_expenses()

    print()
    print("--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("Date\t\tCategory\tAmount\tNote")

    for item in expenses:
        print(
            item["date"], "\t",
            item["category"], "\t\t",
            item["amount"], "\t",
            item["note"]
        )
