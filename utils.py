from storage import expenses



def add_expenses(expenses):
    print("welcome to add expenses section")
    product_name = input("enter the name of the product: ").lower().strip()
    if product_name == "":
        print("error, cannot be blank, please try again!")
        return

    product_amount = input(f"enter the amount of {product_name}: ")
    if  product_amount == "":
        print("error, cannot be blank, please try again!")
        add_expenses(expenses)
        return

    if not product_amount.isdigit():
        print("error, invalid amount, please try again!")
        add_expenses(expenses)
        return

    amount = int(product_amount)
    expenses[product_name] = amount
    print("your expenses have been added")
    print(expenses)
    return




def show_expenses():
    print("welcome to show expenses section")
    for product_name, amount in expenses.items():
        print("product name", product_name)
        print("size", amount)
        



#day 3
def show_total(expenses):
    print("welcome to show total section")

    total_amount = 0
    for amount in expenses.values():
        total_amount += amount

    return total_amount


result = show_total(expenses)
print(result)




def delete_expenses(expenses):

    while True:
        print("welcome to delete expenses section")
        print("type the following to choose your option")

        print("press 1: to delete expenses section")
        print("press 2: to delete all expenses section")


        delete_option = input("->: ").lower().strip()

        if delete_option == "":
            print("error, invalid option, please try again!")
            continue

        elif delete_option == 1:
            print("welcome to delete expenses section")
            product_name = input("enter the name of the product: ").lower().strip()
            if product_name in expenses:
                del expenses[product_name]
                print(f"{product_name}'s expenses have been deleted")
            else:
                print(f"{product_name} has not been found in database")
                continue

        elif delete_option == 2:
            print("welcome to delete all expenses section")
            print("type 'yes' to confirm delete all expenses section")

            confirm = input("enter your choice: ").lower().strip()
            if confirm == "yes":
                expenses.clear()
                print("all expenses have been deleted")

            else:
                print("deletion cancelled")
                continue




















