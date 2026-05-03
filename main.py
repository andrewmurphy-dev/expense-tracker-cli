from utils import add_expenses, show_expenses, show_total, delete_expenses

def cli_expenses():

    while True:
        print("welcome to Command Line Interface: User expenses")
        print("type the following to choose your option")

        print("press 1: Add expenses")
        print("press 2: Show expenses")
        print("press 3: Show total")
        print("press 4: to delete expenses")
        print("press: `exit` to end")

        user_input = input("->: ").lower().strip()

        if user_input == "":
            print("error, cannot be blank, please try again!")
            continue

        elif user_input == "1":
            add_expenses()

        elif user_input == "2":
            show_expenses()

        elif user_input == "3":
            show_total()

        elif user_input == "4":
            delete_expenses()


        elif user_input == "exit":
            print("cli_expensis: thank you for your time, goodbye!")
            break

        else:
            print("error, start again!")
            continue



if __name__ == "__main__":
    cli_expenses()

