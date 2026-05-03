#understanding

expenses = {
    "coffee": 300,
    "train": 220,
    "food": 800
}


expenses = {}


def open_file():
    with open("expenses_test.txt", "w", encoding="utf-8") as f:
        for product_text, amount_text in expenses.items():
            f.write(f"{product_text}{amount_text}\n")


open_file()


#you need to call the file !

def save_expenses():
    loaded = {}

    try:
        with open("expenses_test.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue


        product_text, amount_text = line.split(",",1)
        loaded[product_text] = int(amount_text)
    except FileNotFoundError:
        pass

    return loaded

loaded = save_expenses()
print(loaded)



`