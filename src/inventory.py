import pandas as pd
from src.utils import DATA_DIR, ensure_directory_exists
import os

DATABASE_FILE = os.path.join(DATA_DIR, "database.csv")

class Inventory:
    def __init__(self):
        ensure_directory_exists(DATA_DIR)  # Ensure 'data' directory exists
        self.items = self.load_inventory()

    def load_inventory(self):
        inventory = {}
        try:
            df = pd.read_csv(DATABASE_FILE)
            for _, row in df.iterrows():
                item_id = row["ItemID"]
                inventory[item_id] = {
                    "name": row["Name"],
                    "quantity": int(row["Quantity"]),
                    "price": float(row["Price"]),
                }
        except FileNotFoundError:
            df = pd.DataFrame(
                columns=["ItemID", "Name", "Quantity", "Price"]
            )  # Define columns
            df.to_csv(DATABASE_FILE, index=False)
        return inventory

    def save_inventory(self):
        data = []
        for item_id, item in self.items.items():
            data.append(
                {
                    "ItemID": item_id,
                    "Name": item["name"],
                    "Quantity": item["quantity"],
                    "Price": item["price"],
                }
            )
        df = pd.DataFrame(data)
        df.to_csv(DATABASE_FILE, index=False)

    def view_inventory(self):
        return self.items

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            return "Item ID already exists."
        else:
            self.items[item_id] = {"name": name, "quantity": quantity, "price": price}
            self.save_inventory()
            return "Item added successfully."

    def update_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            self.items[item_id] = {"name": name, "quantity": quantity, "price": price}
            self.save_inventory()
            return "Item updated."
        else:
            return "Item not found."

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            self.save_inventory()
            return "Item deleted."
        else:
            return "Item not found."
