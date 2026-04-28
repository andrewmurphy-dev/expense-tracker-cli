
expenses = {}

def save_expenses():
    with open("expenses_data.txt", "w", encoding="utf-8") as f:
        for product_name, amount in expenses.items():
            f.write(f"{product_name}{amount}\n")



            
            product_name, amount_text = line.split(",",1)
            loaded[product_name] = int[amount_text]

    except FileNotFoundError:
        pass

    return loaded 

