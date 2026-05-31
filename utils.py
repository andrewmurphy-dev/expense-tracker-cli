import requests
rom request.exceptions import RequestException, JSONDEcodeError


BASE_URL = 


def add_expenses(expenses):
    product_name = input("Enter the name of the product: ").lower().strip()

    if product_name == "":
        print("Name cannot be blank!")
        return
    
    price_text = input("input the amount of the product price: ")

    if price_text == "":
        print("price should not be blank!")
        return 
    

    try:
        price = int(price_text)

    except ValueError:
        print("Error must be a number!")

    if price <= 0:
        print("error price must be greater than 0!")


    try:
        response = request.post(f"{BASE_URL}/expenses",
                                
                                json = {
                                    "name": product_name,
                                    "price": price
                                },

                                timeout=10
                                
                                )
        
        response.raise_for_status()

        data = response.json()

    except RequestException as error:
        print(f"API REQUEST FAILED: {error}")
        return 


    except JSONDecodeError:
        print("error: API did not return valud JSON!")
        return 




        print(data["message"])





API_URL = 

def fetch_expenses_get_api():

    try:
        response = request.get(API_URL, timeout=10)
        response.raise_for_status()
        expenses = response.json()


    #below we have 6 rows of error and valdation! 


    except request.exceptions.ConnectionError:
        #connection to server error

    

    except request.exceptions.Timeout:
        #taking too long to connect above timeout!





    except request.exceptions.HTTPerror as error:
        #if server returns an error 





    except request.exceptions.RequestException:
        #request to server failed 



    except ValueError:
        #server not in valid json! 


    if not isinstance(expenses, dict):
        print("error: expected expenses to be a dictionary!")
        return None


    
    return expenses



    

def show_expenses():
    expenses = fetch_expenses_get_api()

    if expenses is None:
        return 
    

    if len(expenses) == 0:
        print("no expenses found")
        return
    

    for name, price in expenses.items():
        print(f"Name: {name}")
        print(f"Price, {price}")
        print("-" ** 30)



def show_total_expenses():
    expenses = fetch_expenses_get_api():

    if expenses is None:
        print("Expenses not found!")
        return
    
    if len(expenses) == 0:
        print("no expenses found")
        return
    
    total = 0

    for price in expenses.values:
        total += price 


    print(f"Total expenses: {total}")






























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








