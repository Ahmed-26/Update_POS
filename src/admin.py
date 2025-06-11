import pandas as pd
from src.utils import DATA_DIR, ensure_directory_exists
    
import os 

ADMIN_DATA_FILE = os.path.join(DATA_DIR, "admin_data.csv")
SECURITY_QUESTION = "What is your favorite color?"
SECURITY_ANSWER = "blue"


class Admin:
    SECURITY_QUESTION = "What is your favorite color?"
    SECURITY_ANSWER = "blue"
    def __init__(self):
        ensure_directory_exists(DATA_DIR)
        self.data = self.load_admin_data()

    def load_admin_data(self):
        try:
            df = pd.read_csv(ADMIN_DATA_FILE,dtype=str)
            return {"username": df["username"][0], "password": df["password"][0]}
        except (FileNotFoundError, KeyError, IndexError):
            self.set_admin_data("admin", "password")
            return {"username": "admin", "password": "password"}

    def set_admin_data(self, username, password):
        df = pd.DataFrame({"username": [username], "password": [password]})
        df.to_csv(ADMIN_DATA_FILE, index=False)
        self.data = {"username": username, "password": password}

    def verify_login(self, username, password):
        return username == self.data["username"] and password == self.data["password"]
