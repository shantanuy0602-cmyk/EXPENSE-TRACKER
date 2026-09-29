from data import get_expenses


def total_expense():
    expenses = get_expenses()
    total = 0

    for item in expenses:
        total = total + item["amount"]

    print()
    print("Total Expense =", total)


def category_report():
    expenses = get_expenses()
    categories = {}

    for item in expenses:
        category = item["category"]
        amount = item["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    print()
    print("--- Category Report ---")

    if len(categories) == 0:
        print("No expenses found.")
        return

    for category in categories:
        print(category, "=", categories[category])
