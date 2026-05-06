def add_expenses(expenses):
    product_name = input("Enter the name of the product: ").lower().strip()

    if product_name == "":
        print("Error: cannot be blank. Please try again.")
        return

    product_amount = input(f"Enter amount of {product_name}: ").strip()

    if product_amount == "":
        print("Error: cannot be blank. Please try again.")
        return

    if not product_amount.isdigit():
        print("Error: invalid amount. Please try again.")
        return

    amount = int(product_amount)

    expenses[product_name] = amount
    print("Your expense has been added.")


def show_expenses(expenses):
    print()
    print("Show expenses")
    print("-" * 30)

    if not expenses:
        print("No expenses found.")
        return

    for product_name, amount in expenses.items():
        print("Product name:", product_name)
        print("Amount:", amount)
        print("-" * 30)


def show_total(expenses):
    print()
    print("Total expenses")
    print("-" * 30)

    total_amount = 0

    for amount in expenses.values():
        total_amount += amount

    print(f"Total: {total_amount}")
    return total_amount


def delete_expenses(expenses):
    while True:
        print()
        print("Welcome to delete expenses section")
        print("Type the following to choose your option")
        print("Press 1: Delete one expense")
        print("Press 2: Delete all expenses")
        print("Press exit: Go back to main menu")

        delete_option = input("->: ").lower().strip()

        if delete_option == "":
            print("Error: invalid option. Please try again.")
            continue

        elif delete_option == "1":
            product_name = input("Enter the name of the product: ").lower().strip()

            if product_name == "":
                print("Error: product name cannot be blank.")
                continue

            if product_name in expenses:
                del expenses[product_name]
                print(f"{product_name}'s expense has been deleted.")
                break
            else:
                print(f"{product_name} was not found.")
                continue

        elif delete_option == "2":
            print("Type 'yes' to confirm deleting all expenses.")

            confirm = input("Enter your choice: ").lower().strip()

            if confirm == "yes":
                expenses.clear()
                print("All expenses have been deleted.")
                break
            else:
                print("Deletion cancelled.")
                break

        elif delete_option == "exit":
            print("Returning to main menu.")
            break

        else:
            print("Error: invalid option. Please try again.")








