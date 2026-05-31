import requests
from requests.exceptions import RequestException, JSONDecodeError

BASE_URL = "http://127.0.0.1:8000"


def add_expenses():
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
        response = requests.post(f"{BASE_URL}/expenses",
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








API_URL = "http://127.0.0.1:8000"

def fetch_expenses_get_api():

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        expenses = response.json()


    except requests.exceptions.ConnectionError:
        print("error: connection to derver was not viable!")
        return

    except requests.exceptions.Timeout:
        print("error: server connection exceeded timeout!")
        return

    except requests.exceptions.HTTPerror as error:
        print(f"error: server has returned a {error}")
        return

    except requests.exceptions.RequestException:
        print("error: server request failed!")

    except ValueError:
        print("server is not in valid JSON format!")
        return
     

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
    expenses = fetch_expenses_get_api()

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











def delete_expenses():

    expense_name = input("enter the name of the product you wish to delete: ")

    if expense_name == "":
        print("product cannot be blank!")
        return 
    
    try: 
        response = requests.delete(f"{API_URL}/expenses/{expense_name}, timeout=10")
        response.raise_for_status
        data = response.json()

    except RequestException as error:
        print(f"API REQUEST FAILED: {error}")
        return 


    except JSONDecodeError:
        print("error: API did not return valud JSON!")
        return 
        
    print(data["message"])









