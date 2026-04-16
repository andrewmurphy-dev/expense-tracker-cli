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
        print(product_name, amount)



#day 3
def show_total(expenses):
    total_amount = 0

    for amount in expenses.values():
        total_amount += amount

    return total_amount


result = show_total(expenses)
print(result)






