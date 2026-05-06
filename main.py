from storage import load_expenses, save_expenses
from utils import add_expenses, show_expenses, show_total, delete_expenses


def cli_expenses():
    expenses = load_expenses()

    while True:
        print("Welcome to Command Line Interface: User Expenses")
        print("Type the following to choose your option")
        print("Press 1: Add expense")
        print("Press 2: Show expenses")
        print("Press 3: Show total")
        print("Press 4: Delete expense")
        print("Type exit: End program")

        user_input = input("->: ").lower().strip()

        if user_input == "":
            print("Error: cannot be blank. Please try again.")
            continue

        elif user_input == "1":
            add_expenses(expenses)
            save_expenses(expenses)

        elif user_input == "2":
            show_expenses(expenses)

        elif user_input == "3":
            show_total(expenses)

        elif user_input == "4":
            delete_expenses(expenses)
            save_expenses(expenses)

        elif user_input == "exit":
            print("cli_expenses: thank you for your time, goodbye!")
            break

        else:
            print("Error: invalid option. Try again.")


if __name__ == "__main__":
    cli_expenses()
