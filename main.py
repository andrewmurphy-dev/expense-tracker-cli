from storage import expenses
from utils import add_expenses, show_expenses,show_total

def cli_expenses():

    while True:
        print("welcome to Command Line Interface: User expenses")
        print("type the following to choose your option")

        print("press 1: Add expenses")
        print("press 2: Show expenses")
        print("press 3: Show total")
        print("press: `exit` to end")

        user_input = input("->: ").lower().strip()

        if user_input == "1":
            print("error, cannot be blank, please try again!")
            continue

        elif user_input == "1":
            add_expenses(expenses)

        elif user_input == "2":
            show_expenses()

        elif user_input == "3":
            show_total(expenses)

        elif user_input == "exit":
            print("cli_expensis: thank you for your time, goodbye!")
            continue

        else:
            print("error, start again!")
            continue



cli_expenses()

