# import os
# import io
# import datetime
# import textwrap
# import streamlit as st
# import pandas as pd
# from PIL import Image, ImageDraw, ImageFont

# # Constants
# DATABASE_FILE = "database.txt"
# ADMIN_DATA_FILE = "admin_data.txt"
# SECURITY_QUESTION = "What is your favorite color?"
# SECURITY_ANSWER = "blue"


# class Admin:
#     def __init__(self):
#         self.data = self.load_admin_data()

#     def load_admin_data(self):
#         try:
#             with open(ADMIN_DATA_FILE, "r") as file:
#                 data = file.readline().strip().split("|")
#                 return {"username": data[0], "password": data[1]}
#         except FileNotFoundError:
#             self.set_admin_data("admin", "password")
#             return {"username": "admin", "password": "password"}

#     def set_admin_data(self, username, password):
#         with open(ADMIN_DATA_FILE, "w") as file:
#             file.write(f"{username}|{password}\n")
#         self.data = {"username": username, "password": password}

#     def verify_login(self, username, password):
#         return username == self.data["username"] and password == self.data["password"]


# class Inventory:
#     def __init__(self):
#         self.items = self.load_inventory()

#     def load_inventory(self):
#         inventory = {}
#         try:
#             with open(DATABASE_FILE, "r") as file:
#                 lines = file.readlines()[1:]
#                 for line in lines:
#                     parts = line.strip().split("|")
#                     if len(parts) == 4:
#                         item_id, name, quantity, price = parts
#                         inventory[item_id] = {
#                             "name": name,
#                             "quantity": int(quantity),
#                             "price": float(price),
#                         }
#         except FileNotFoundError:
#             with open(DATABASE_FILE, "w") as file:
#                 file.write("ItemID|Name|Quantity|Price\n")
#         return inventory

#     def save_inventory(self):
#         with open(DATABASE_FILE, "w") as file:
#             file.write("ItemID|Name|Quantity|Price\n")
#             for item_id, item in self.items.items():
#                 file.write(
#                     f"{item_id}|{item['name']}|{item['quantity']}|{item['price']:.2f}\n"
#                 )

#     def view_inventory(self):
#         return self.items

#     def add_item(self, item_id, name, quantity, price):
#         if item_id in self.items:
#             return "Item ID already exists."
#         else:
#             self.items[item_id] = {"name": name, "quantity": quantity, "price": price}
#             self.save_inventory()
#             return "Item added successfully."

#     def update_item(self, item_id, name, quantity, price):
#         if item_id in self.items:
#             self.items[item_id] = {"name": name, "quantity": quantity, "price": price}
#             self.save_inventory()
#             return "Item updated."
#         else:
#             return "Item not found."

#     def delete_item(self, item_id):
#         if item_id in self.items:
#             del self.items[item_id]
#             self.save_inventory()
#             return "Item deleted."
#         else:
#             return "Item not found."


# class SalesLogger:
#     def __init__(self, receipt_file="sales_receipt.txt", daily_file="daily_sales.txt"):
#         self.receipt_file = receipt_file
#         self.daily_file = daily_file
#         self.ensure_file_exists(self.daily_file)

#     def ensure_file_exists(self, file_path):
#         if not os.path.exists(file_path):
#             with open(file_path, "w") as file:
#                 file.write("Date | Item Name | Quantity Sold | Total Sales\n")

#     def record_receipt(self, item_name, quantity, unit_price):
#         now = datetime.datetime.now()
#         total_price = quantity * unit_price
#         with open(self.receipt_file, "a") as file:
#             file.write(
#                 f"{now} | {item_name} | Qty: {quantity} | Unit: {unit_price:.2f} | Total: {total_price:.2f}\n"
#             )

#     def update_daily_sales(self, item_name, quantity, total_price):
#         date = datetime.datetime.now().strftime("%Y-%m-%d")
#         with open(self.daily_file, "a") as file:
#             file.write(
#                 f"{date} | {item_name} | Sold: {quantity} | Total: {total_price:.2f}\n"
#             )


# def receipt_text_to_png(receipt_text):
#     MAX_LINE_LENGTH = 60  # max chars per line before wrap

#     lines = []
#     for line in receipt_text.splitlines():
#         wrapped = textwrap.wrap(line, width=MAX_LINE_LENGTH) or [""]
#         lines.extend(wrapped)

#     font_path = None
#     try:
#         import sys

#         if sys.platform == "win32":
#             font_path = "C:\\Windows\\Fonts\\consola.ttf"
#         elif sys.platform == "darwin":
#             font_path = "/System/Library/Fonts/Menlo.ttc"
#         else:
#             font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
#         font_size = 16
#         font = ImageFont.truetype(font_path, font_size)
#     except:
#         font_size = 16
#         font = ImageFont.load_default()

#     max_width = 0
#     line_height = None

#     def text_size(text, font):
#         if hasattr(font, "getsize"):
#             return font.getsize(text)
#         bbox = font.getbbox(text)
#         return (bbox[2] - bbox[0], bbox[3] - bbox[1])

#     for line in lines:
#         w, h = text_size(line, font)
#         max_width = max(max_width, w)
#         if line_height is None or h > line_height:
#             line_height = h
#     if line_height is None:
#         line_height = font_size + 2

#     padding_x = 15
#     padding_y = 15
#     img_height = line_height * len(lines) + padding_y * 2
#     img_width = max_width + padding_x * 2

#     max_img_width = 480
#     if img_width > max_img_width:
#         img_width = max_img_width

#     image = Image.new("RGB", (img_width, img_height), color="white")
#     draw = ImageDraw.Draw(image)
#     y = padding_y
#     for line in lines:
#         draw.text((padding_x, y), line, fill="black", font=font)
#         y += line_height

#     buffer = io.BytesIO()
#     image.save(buffer, format="PNG")
#     buffer.seek(0)
#     return buffer


# def load_admin():
#     if "admin" not in st.session_state:
#         st.session_state.admin = Admin()
#     return st.session_state.admin


# def load_inventory():
#     if "inventory" not in st.session_state:
#         st.session_state.inventory = Inventory()
#     return st.session_state.inventory


# def load_sales_logger():
#     if "sales_logger" not in st.session_state:
#         st.session_state.sales_logger = SalesLogger()
#     return st.session_state.sales_logger


# def main():
#     st.set_page_config(page_title="Inventory Management System", layout="wide")

#     admin = load_admin()
#     inventory = load_inventory()
#     sales_logger = load_sales_logger()

#     if "sale_completed" not in st.session_state:
#         st.session_state.sale_completed = False
#     if "receipt_text" not in st.session_state:
#         st.session_state.receipt_text = ""
#     if "sale_items" not in st.session_state:
#         st.session_state.sale_items = []
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#     if "logged_out" not in st.session_state:
#         st.session_state.logged_out = False
#     if "pwd_recovery_stage" not in st.session_state:
#         st.session_state.pwd_recovery_stage = None
#     if "recovery_username" not in st.session_state:
#         st.session_state.recovery_username = ""

#     if not st.session_state.logged_in:
#         if st.session_state.logged_out:
#             st.success("You have successfully logged out.")
#             st.session_state.logged_out = False  # Reset after showing

#         st.title("Admin Login")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             if admin.verify_login(username, password):
#                 st.session_state.logged_in = True
#                 st.session_state.pwd_recovery_stage = None
#                 st.session_state.recovery_username = ""
#             else:
#                 st.error("Invalid username or password.")

#         st.markdown("### Forgot Password?")

#         # Password recovery flow with staged session_state
#         if st.session_state.pwd_recovery_stage is None:
#             recover_username_input = st.text_input(
#                 "Enter username for password recovery"
#             )
#             if st.button("Recover Password"):
#                 if recover_username_input == admin.data["username"]:
#                     st.session_state.pwd_recovery_stage = "awaiting_answer"
#                     st.session_state.recovery_username = recover_username_input
#                     st.experimental_rerun()
#                 else:
#                     st.error("Username not found.")
#         elif st.session_state.pwd_recovery_stage == "awaiting_answer":
#             st.write(f"Security Question: {SECURITY_QUESTION}")
#             answer = st.text_input("Your Answer")
#             if st.button("Submit Answer"):
#                 if answer and answer.lower() == SECURITY_ANSWER:
#                     st.session_state.pwd_recovery_stage = "answer_correct"
#                     st.experimental_rerun()
#                 else:
#                     st.error("Incorrect answer!")
#         elif st.session_state.pwd_recovery_stage == "answer_correct":
#             new_password = st.text_input("Enter new password", type="password")
#             confirm_password = st.text_input("Confirm new password", type="password")
#             if st.button("Change Password"):
#                 if not new_password or not confirm_password:
#                     st.error("Please enter and confirm your new password.")
#                 elif new_password != confirm_password:
#                     st.error("Passwords do not match!")
#                 else:
#                     admin.set_admin_data(
#                         st.session_state.recovery_username, new_password
#                     )
#                     st.success(
#                         "Password changed successfully! Please log in with your new password."
#                     )
#                     st.session_state.pwd_recovery_stage = None
#                     st.session_state.recovery_username = ""
#                     st.session_state.admin = Admin()
#         return

#     st.sidebar.title("Navigation")
#     options = ["Home", "Inventory Management", "Sales", "Logout"]
#     choice = st.sidebar.radio("Go to", options)

#     if choice == "Logout":
#         st.session_state.logged_out = True
#         st.session_state.logged_in = False
#         st.session_state.sale_items = []
#         st.session_state.receipt_text = ""
#         st.session_state.sale_completed = False

#     if choice == "Home":
#         st.title("Welcome to the POS System (Streamlit Version)")
#         st.info("Use the sidebar to navigate through the app.")
#         try:
#             logo_image = Image.open("logo.png")  # Your logo path here
#             col1, col2, col3 = st.columns([1, 2, 1])
#             with col2:
#                 st.image(logo_image, use_container_width=False, width=350)
#         except Exception as e:
#             st.warning(f"Logo image could not be loaded: {e}")

#     elif choice == "Inventory Management":
#         st.title("Inventory Management")

#         if st.button("Refresh Inventory"):
#             st.session_state.inventory = Inventory()
#             st.success("Inventory refreshed from file.")

#         items = st.session_state.inventory.view_inventory()
#         if items:
#             df = pd.DataFrame.from_dict(items, orient="index")
#             df.index.name = "Item ID"
#             st.dataframe(df)
#             with st.expander("Add New Item"):
#                 id_new = st.text_input("Item ID", key="add_id")
#                 name_new = st.text_input("Name", key="add_name")
#                 quantity_new = st.number_input(
#                     "Quantity", min_value=0, step=1, key="add_qty"
#                 )
#                 price_new = st.number_input(
#                     "Price", min_value=0.0, format="%.2f", key="add_price"
#                 )
#                 if st.button("Add Item"):
#                     if id_new.strip() and name_new.strip():
#                         msg = st.session_state.inventory.add_item(
#                             id_new.strip(), name_new.strip(), quantity_new, price_new
#                         )
#                         st.success(msg)
#                         st.session_state.item_added = True
#                     else:
#                         st.error("Item ID and Name are required.")
#             with st.expander("Update or Delete Item"):
#                 update_id = st.selectbox(
#                     "Select Item ID to Modify", options=list(items.keys()), key="upd_id"
#                 )
#                 if update_id:
#                     item = items[update_id]
#                     new_name = st.text_input("Name", value=item["name"], key="upd_name")
#                     new_quantity = st.number_input(
#                         "Quantity",
#                         min_value=0,
#                         value=item["quantity"],
#                         step=1,
#                         key="upd_qty",
#                     )
#                     new_price = st.number_input(
#                         "Price",
#                         min_value=0.0,
#                         value=item["price"],
#                         format="%.2f",
#                         key="upd_price",
#                     )
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         if st.button("Update Item"):
#                             msg = st.session_state.inventory.update_item(
#                                 update_id, new_name.strip(), new_quantity, new_price
#                             )
#                             st.success(msg)
#                             st.session_state.item_updated = True
#                     with col2:
#                         if st.button("Delete Item"):
#                             msg = st.session_state.inventory.delete_item(update_id)
#                             st.warning(msg)
#                             st.session_state.item_deleted = True
#         else:
#             st.info("Inventory is empty.")

#     elif choice == "Sales":
#         st.title("Sales")
#         items = inventory.view_inventory()
#         if not items:
#             st.info("Inventory is empty. Please add items before processing sales.")
#         else:
#             df = pd.DataFrame.from_dict(items, orient="index")
#             df.index.name = "Item ID"
#             st.dataframe(df)
#             sale_item_id = st.selectbox(
#                 "Select Item ID to Sell", options=list(items.keys()), key="sale_item_id"
#             )
#             if sale_item_id:
#                 item = items[sale_item_id]
#                 st.markdown(f"**Item Name:** {item['name']}")
#                 st.markdown(f"**Available Quantity:** {item['quantity']}")
#                 st.markdown(f"**Price:** ${item['price']:.2f}")
#                 quantity_to_sell = st.number_input(
#                     "Quantity to Sell",
#                     min_value=1,
#                     max_value=item["quantity"],
#                     step=1,
#                     key="qty_sell",
#                 )
#                 if st.button("Add to Cart"):
#                     idx = next(
#                         (
#                             index
#                             for (index, d) in enumerate(st.session_state.sale_items)
#                             if d["item_id"] == sale_item_id
#                         ),
#                         None,
#                     )
#                     if idx is not None:
#                         new_qty = (
#                             st.session_state.sale_items[idx]["quantity"]
#                             + quantity_to_sell
#                         )
#                         if new_qty > item["quantity"]:
#                             st.error(
#                                 f"Cannot add {quantity_to_sell}. Total quantity exceeds stock."
#                             )
#                         else:
#                             st.session_state.sale_items[idx]["quantity"] = new_qty
#                             st.success(f"Updated quantity for {item['name']} in cart.")
#                     else:
#                         st.session_state.sale_items.append(
#                             {
#                                 "item_id": sale_item_id,
#                                 "name": item["name"],
#                                 "quantity": quantity_to_sell,
#                                 "price": item["price"],
#                             }
#                         )
#                         st.success(f"Added {item['name']} to cart.")

#             if st.session_state.sale_items:
#                 st.subheader("Items in Cart")
#                 sale_df = pd.DataFrame(st.session_state.sale_items)
#                 sale_df["total_price"] = sale_df["quantity"] * sale_df["price"]
#                 sale_df_display = sale_df[
#                     ["item_id", "name", "quantity", "price", "total_price"]
#                 ].rename(
#                     columns={
#                         "item_id": "Item ID",
#                         "name": "Name",
#                         "quantity": "Quantity",
#                         "price": "Unit Price",
#                         "total_price": "Total Price",
#                     }
#                 )
#                 st.dataframe(
#                     sale_df_display.style.format(
#                         {"Unit Price": "${:,.2f}", "Total Price": "${:,.2f}"}
#                     ),
#                     use_container_width=True,
#                 )

#                 remove_index = st.number_input(
#                     "Enter index of item to remove (starting at 0):",
#                     min_value=0,
#                     max_value=len(st.session_state.sale_items) - 1,
#                     step=1,
#                     key="remove_index",
#                 )

#                 if st.button("Remove Item from Cart"):
#                     removed_item = st.session_state.sale_items.pop(remove_index)
#                     st.warning(f"Removed {removed_item['name']} from cart.")
#                     st.session_state.item_removed_from_cart = True

#                 total_sale = sale_df["total_price"].sum()
#                 st.markdown(f"### Total Sale Amount: ${total_sale:.2f}")

#                 amount_paid = st.number_input(
#                     "Amount Paid by Customer",
#                     min_value=total_sale,
#                     value=total_sale,
#                     format="%.2f",
#                     step=1.0,
#                     key="amount_paid",
#                 )

#                 change = amount_paid - total_sale
#                 st.markdown(f"### Change to Return: ${change:.2f}")

#                 customer_name = st.text_input("Customer Name", key="customer_name")

#                 if st.button("Complete Sale"):
#                     if not customer_name.strip():
#                         st.error("Customer name is required.")
#                     elif amount_paid < total_sale:
#                         st.error("Amount paid cannot be less than total sale amount.")
#                     else:
#                         for sale_item in st.session_state.sale_items:
#                             stock_qty = inventory.items[sale_item["item_id"]][
#                                 "quantity"
#                             ]
#                             if sale_item["quantity"] > stock_qty:
#                                 st.error(
#                                     f"Not enough stock for {sale_item['name']}. Available: {stock_qty}"
#                                 )
#                                 return

#                         receipt_lines = [
#                             "------ SALES RECEIPT ------",
#                             f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
#                             f"Customer Name: {customer_name}",
#                             "",
#                         ]
#                         grand_total = 0
#                         for sale_item in st.session_state.sale_items:
#                             item_id = sale_item["item_id"]
#                             qty = sale_item["quantity"]
#                             price = sale_item["price"]
#                             total = qty * price
#                             grand_total += total
#                             inventory.items[item_id]["quantity"] -= qty
#                             sales_logger.record_receipt(sale_item["name"], qty, price)
#                             sales_logger.update_daily_sales(
#                                 sale_item["name"], qty, total
#                             )
#                             receipt_lines.append(f"Item: {sale_item['name']}")
#                             receipt_lines.append(f"Quantity: {qty}")
#                             receipt_lines.append(f"Unit Price: {price:.2f}")
#                             receipt_lines.append(f"Total: {total:.2f}")
#                             receipt_lines.append("")
#                         receipt_lines.append(f"Grand Total: {grand_total:.2f}")
#                         receipt_lines.append(f"Amount Paid: {amount_paid:.2f}")
#                         receipt_lines.append(f"Change Returned: {change:.2f}")
#                         receipt_lines.append("\nThank you for your purchase!")
#                         inventory.save_inventory()
#                         st.success("Sale completed successfully!")

#                         st.session_state.receipt_text = "\n".join(receipt_lines)
#                         st.session_state.sale_completed = True
#                         st.session_state.sale_items = []

#                 if st.session_state.sale_completed and st.session_state.receipt_text:
#                     st.markdown("### Receipt")
#                     st.text_area(
#                         "Receipt Text",
#                         st.session_state.receipt_text,
#                         height=300,
#                         key="receipt_display",
#                     )

#                     png_buffer = receipt_text_to_png(st.session_state.receipt_text)

#                     st.download_button(
#                         label="Download Receipt as PNG",
#                         data=png_buffer,
#                         file_name="receipt.png",
#                         mime="image/png",
#                         key="download_receipt",
#                     )

#     # Reset item action flags
#     for key in [
#         "item_added",
#         "item_updated",
#         "item_deleted",
#         "item_removed_from_cart",
#     ]:
#         if st.session_state.get(key, False):
#             st.session_state[key] = False


# if __name__ == "__main__":
#     main()
