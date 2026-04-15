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
        return

    amount = int(product_amount)

    expenses[product_name] = amount
    print("your expenses have been added", expenses)










def show_expenses():
    for product_name, amount in expenses.items():
        print(product_name, amount)


#day 3
def show_total():
    total_amount = []
    for product_name, amount in expenses.values():
        total_amount += 1
        print(total_amount)


