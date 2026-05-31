
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




                           
                           
                           
                           
                           
                           

                    




#confusion i dont think i send a json request , i think its just a string !
                           
                          