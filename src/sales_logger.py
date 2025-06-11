import pandas as pd
import datetime
import os
from src.utils import DATA_DIR, ensure_directory_exists

RECEIPT_FILE = os.path.join(DATA_DIR, "sales_receipt.csv")
DAILY_SALES_FILE = os.path.join(DATA_DIR, "daily_sales.csv")


class SalesLogger:
    def __init__(self, receipt_file="data/sales_receipt.csv", daily_file="data/daily_sales.csv"):
        self.receipt_file = receipt_file
        self.daily_file = daily_file
        self.ensure_file_exists(self.daily_file)
    def ensure_file_exists(self, file_path):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            # Create a new DataFrame with the correct columns
            df = pd.DataFrame(columns=["Date", "Item Name", "Quantity Sold", "Total Sales"])
            df.to_csv(file_path, index=False)

    def record_receipt(self, item_name, quantity, unit_price):
        now = datetime.datetime.now()
        total_price = quantity * unit_price
        df = pd.DataFrame(
            [
                {
                    "Date": now,
                    "Item Name": item_name,
                    "Quantity": quantity,
                    "Unit Price": unit_price,
                    "Total": total_price,
                }
            ]
        )
        df.to_csv(self.receipt_file, mode="a", header=not os.path.exists(self.receipt_file), index=False)

    def update_daily_sales(self, item_name, quantity, total_price):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        df = pd.DataFrame(
            [
                {
                    "Date": date,
                    "Item Name": item_name,
                    "Quantity Sold": quantity,
                    "Total Sales": total_price,
                }
            ]
        )
        df.to_csv(self.daily_file, mode="a", header=not os.path.exists(self.daily_file), index=False)
