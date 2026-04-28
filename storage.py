

expenses = {}

def save_expenses():
    with open("expenses_data.txt", "w", encoding="utf-8") as f:
        for product_name, amount in expenses.items():
            f.write(f"{product_name}{amount}\n")


    
def load_expenses():
    loaded = {} 

    try:
        with open("expenses_data.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = f.strip()
                #got this wrong , neeeds to be line.strip() its each line in the variable loop 
                if line == "":
                    continue


            
            product_name, amount_text = line.split(",",1)
            loaded[product_name] = int[amount_text]

    except FileNotFoundError:
        pass

    return loaded 



