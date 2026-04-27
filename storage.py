import pathlib

# Same folder as this file: plain text, one line per item "name|amount"
DATA_FILE = pathlib.Path(__file__).with_name("expenses_data.txt")

# Single dict shared by the app; we mutate in place so imports keep the same object.
expenses: dict = {}


def load_expenses() -> None:
    """Fill `expenses` from disk. Uses the same dict object (safe for 'from storage import')."""
    expenses.clear()
    if not DATA_FILE.is_file():
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue
            name, _, amount_str = line.partition("|")
            name = name.strip()
            amount_str = amount_str.strip()
            if name and amount_str.isdigit():
                expenses[name] = int(amount_str)


def save_expenses() -> None:
    """Write the whole `expenses` dict to disk (overwrite)."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for name, amount in expenses.items():
            f.write(f"{name}|{amount}\n")


load_expenses()
