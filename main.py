from menu import show_menu
from expense import add_expense, view_expenses
from report import total_expense, category_report
from data import clear_data

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_report()
    elif choice == "5":
        clear_data()
    elif choice == "6":
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid choice.")
