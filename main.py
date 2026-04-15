from storage import expenses
from utils import add_expenses, show_expenses

def cli_expenses():

    while True:
        print("welcome to Command Line Interface: User expenses")
        print("type the following to choose your option")

        print("press 1: Add expenses")
        print("press 2: Show expenses")
        print("press 3: Show total")
        print("press: `exit` to end")

        x_input = input("->: ").lower().strip()

        if x_input == "":
            print("error, cannot be black, please try again!")

        elif x_input == "1":
            add_expenses(expenses)


        elif x_input == "2":
            show_expenses()



        elif x_input == "3":


        elif x_input == "exit":
            print("cli_expensis: thank you for your time, goodbye!")
            break

        else:
            print("error, start again!")
            return


cli_expenses()


