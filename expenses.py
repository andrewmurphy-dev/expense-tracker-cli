import requests
from request.exceptions import RequestException, JSONDEcodeError


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



