expenses = {
    "coffee": 300,
    "train": 220,
    "food": 800
}



def save_expenses():
    with open("expenses_data.txt", "w", encoding="utf-8") as f:
        for product_name, amount in expenses.items():
            f.write(f"{product_name},{amount}\n")


def load_expenses():
    loaded = {}

    try:
        with open("expenses_data.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                product_name, amount = line.split(",", 1)
                #this actually comes from , for line in f 
                #for line in f is reading in text format 
                loaded[product_name] = int(amount)

    except FileNotFoundError:
        pass

    return loaded




save_expenses()

loaded_data = load_expenses()
print(loaded_data)

