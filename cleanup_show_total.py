import requests 


#show expenses we need to use get method i assume , because we want to get the data ! 
#its very important that we use try , except for this situation ! 
#this would be a real world example




#so we are gonna make a general function to call the data in the endpoint 


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

