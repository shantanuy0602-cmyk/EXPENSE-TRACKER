FILE_NAME = "expenses.txt"


def save_expense(date, category, amount, note):
    file = open(FILE_NAME, "a")
    file.write(date + "|" + category + "|" + str(amount) + "|" + note + "\n")
    file.close()


def get_expenses():
    expenses = []

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            line = line.strip()

            if line != "":
                parts = line.split("|")

                if len(parts) == 4:
                    expense = {
                        "date": parts[0],
                        "category": parts[1],
                        "amount": float(parts[2]),
                        "note": parts[3]
                    }
                    expenses.append(expense)

        file.close()

    except FileNotFoundError:
        pass

    return expenses


def clear_data():
    choice = input("Are you sure you want to clear all expenses? (yes/no): ")

    if choice.lower() == "yes":
        file = open(FILE_NAME, "w")
        file.close()
        print("All expenses deleted.")
    else:
        print("Data was not deleted.")
