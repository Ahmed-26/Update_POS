# import os
# import datetime
# import tkinter as tk
# from tkinter import messagebox, simpledialog, ttk, scrolledtext, filedialog

# # Add Pillow imports for image creation
# from PIL import Image, ImageDraw, ImageFont

# DATABASE_FILE = 'database.txt'
# ADMIN_DATA_FILE = 'admin_data.txt'
# SECURITY_QUESTION = "What is your favorite color?"
# SECURITY_ANSWER = "blue"

# class Admin:
#     def __init__(self):
#         self.data = self.load_admin_data()

#     def load_admin_data(self):
#         try:
#             with open(ADMIN_DATA_FILE, 'r') as file:
#                 data = file.readline().strip().split('|')
#                 return {'username': data[0], 'password': data[1]}
#         except FileNotFoundError:
#             self.set_admin_data('admin', 'password')
#             return {'username': 'admin', 'password': 'password'}

#     def set_admin_data(self, username, password):
#         with open(ADMIN_DATA_FILE, 'w') as file:
#             file.write(f"{username}|{password}\n")

#     def verify_login(self, username, password):
#         return username == self.data['username'] and password == self.data['password']

#     def forgot_password(self, username):
#         if username == self.data['username']:
#             answer = simpledialog.askstring("Security Question", SECURITY_QUESTION)
#             if answer and answer.lower() == SECURITY_ANSWER:
#                 messagebox.showinfo("Password Recovery", "Your password is: 'password'. Please update it after login.")
#             else:
#                 messagebox.showerror("Error", "Incorrect answer!")
#         else:
#             messagebox.showerror("Error", "Username not found.")

# class Inventory:
#     def __init__(self):
#         self.items = self.load_inventory()

#     def load_inventory(self):
#         inventory = {}
#         try:
#             with open(DATABASE_FILE, 'r') as file:
#                 lines = file.readlines()[1:]
#                 for line in lines:
#                     item_id, name, quantity, price = line.strip().split('|')
#                     inventory[item_id] = {'name': name, 'quantity': int(quantity), 'price': float(price)}
#         except FileNotFoundError:
#             pass
#         return inventory

#     def save_inventory(self):
#         with open(DATABASE_FILE, 'w') as file:
#             file.write("ItemID|Name|Quantity|Price\n")
#             for item_id, item in self.items.items():
#                 file.write(f"{item_id}|{item['name']}|{item['quantity']}|{item['price']:.2f}\n")

#     def view_inventory(self):
#         return self.items

#     def add_item(self, item_id, name, quantity, price):
#         if item_id in self.items:
#             return "Item ID already exists."
#         else:
#             self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}
#             self.save_inventory()
#             return "Item added successfully."

#     def update_item(self, item_id, name, quantity, price):
#         if item_id in self.items:
#             self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}
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
#     def __init__(self, receipt_file='sales_receipt.txt', daily_file='daily_sales.txt'):
#         self.receipt_file = receipt_file
#         self.daily_file = daily_file
#         self.ensure_file_exists(self.daily_file)

#     def ensure_file_exists(self, file_path):
#         if not os.path.exists(file_path):
#             with open(file_path, 'w') as file:
#                 file.write("Date | Item Name | Quantity Sold | Total Sales\n")

#     def record_receipt(self, item_name, quantity, unit_price):
#         now = datetime.datetime.now()
#         total_price = quantity * unit_price
#         with open(self.receipt_file, 'a') as file:
#             file.write(f"{now} | {item_name} | Qty: {quantity} | Unit: {unit_price:.2f} | Total: {total_price:.2f}\n")

#     def update_daily_sales(self, item_name, quantity, total_price):
#         date = datetime.datetime.now().strftime('%Y-%m-%d')
#         with open(self.daily_file, 'a') as file:
#             file.write(f"{date} | {item_name} | Sold: {quantity} | Total: {total_price:.2f}\n")

# class POSSystem:
#     def __init__(self, root):
#         self.admin = Admin()
#         self.inventory = Inventory()
#         self.sales_logger = SalesLogger()
#         self.logged_in = False

#         self.root = root
#         self.root.title("POS System")
#         self.root.geometry("720x600")
#         self.root.resizable(False, False)

#         self.style = ttk.Style()
#         self.style.theme_use('clam')

#         self.style.configure('TButton',
#                              font=('Segoe UI', 10),
#                              borderwidth=1,
#                              relief='raised',
#                              background='#4a90e2',
#                              foreground='white',
#                              padding=8)
#         self.style.map('TButton',
#                        background=[('active', '#357ABD'), ('disabled', '#a6a6a6')],
#                        foreground=[('disabled', '#666666')])
#         self.style.configure('Danger.TButton',
#                              background='#d9534f',
#                              foreground='white')
#         self.style.map('Danger.TButton',
#                        background=[('active', '#c9302c')])
#         self.style.configure('Success.TButton',
#                              background='#5cb85c',
#                              foreground='white')
#         self.style.map('Success.TButton',
#                        background=[('active', '#4cae4c')])
#         self.style.configure('TFrame', background='#f0f4f8')
#         self.style.configure('TLabel', background='#f0f4f8')
#         self.style.configure('Treeview', font=('Segoe UI', 10))
#         self.style.configure('Treeview.Heading', font=('Segoe UI', 11,'bold'), background='#4a90e2', foreground='white')

#         self.root.configure(bg='#f0f4f8')

#         self.selected_sale_items = []

#         self.create_widgets()

#     def create_widgets(self):
        
        
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

#         self.home_frame = ttk.Frame(self.notebook)
#         self.notebook.add(self.home_frame, text="Home")
#         ttk.Label(self.home_frame, text="Welcome to POS System!", font=("Segoe UI", 18, "bold"), foreground="#333").pack(pady=30)

        
#         self.login_frame = ttk.Frame(self.notebook)
#         self.notebook.add(self.login_frame, text="Admin Login")

#         # Configure grid columns for centering content
#         self.login_frame.columnconfigure(0, weight=1)
#         self.login_frame.columnconfigure(1, weight=1)

#         login_label = ttk.Label(self.login_frame, text="Please Login", font=("Segoe UI", 16, "bold"), foreground="#222")
#         login_label.grid(row=0, column=0, columnspan=2, pady=(20, 15), sticky="nsew")

#         ttk.Label(self.login_frame, text="Username:", font=('Segoe UI', 11)).grid(row=1, column=0, pady=10, sticky='e', padx=10)
#         self.username_entry = ttk.Entry(self.login_frame, font=('Segoe UI', 11))
#         self.username_entry.grid(row=1, column=1, pady=10, sticky='w', padx=10)

#         ttk.Label(self.login_frame, text="Password:", font=('Segoe UI', 11)).grid(row=2, column=0, pady=10, sticky='e', padx=10)
#         self.password_entry = ttk.Entry(self.login_frame, show='*', font=('Segoe UI', 11))
#         self.password_entry.grid(row=2, column=1, pady=10, sticky='w', padx=10)

#         button_width = 15
#         login_button = ttk.Button(self.login_frame, text="Login", command=self.handle_login, style='Success.TButton', width=button_width)
#         login_button.grid(row=3, column=0, pady=(10, 5), ipadx=10, sticky='ew')

#         forgot_button = ttk.Button(self.login_frame, text="Forgot Password?", command=self.handle_forgot_password, style='TButton', width=button_width)
#         forgot_button.grid(row=3, column=1, pady=(10, 5), ipadx=10, sticky='ew', padx=(10,0))  # Added left padding for gap

#         self.inventory_frame = ttk.Frame(self.notebook, style='TFrame')
#         self.notebook.add(self.inventory_frame, text="Inventory Management")
#         controls_frame = ttk.Frame(self.inventory_frame, style='TFrame')
#         controls_frame.pack(side='top', fill='x', pady=7)
#         self.add_button = ttk.Button(controls_frame, text="Add Item", command=self.show_add_item_dialog, style='Success.TButton')
#         self.add_button.pack(side='left', padx=8)
#         self.update_button = ttk.Button(controls_frame, text="Update Item", command=self.show_update_item_options, style='TButton')
#         self.update_button.pack(side='left', padx=8)
#         self.delete_button = ttk.Button(controls_frame, text="Delete Item", command=self.delete_selected_item, style='Danger.TButton')
#         self.delete_button.pack(side='left', padx=8)
#         self.refresh_button = ttk.Button(controls_frame, text="Refresh Inventory", command=self.refresh_inventory_list, style='TButton')
#         self.refresh_button.pack(side='left', padx=8)
#         self.inventory_tree = ttk.Treeview(self.inventory_frame, columns=("ID", "Name", "Quantity", "Price"), show='headings', selectmode='browse')
#         self.inventory_tree.heading("ID", text="Item ID")
#         self.inventory_tree.heading("Name", text="Name")
#         self.inventory_tree.heading("Quantity", text="Quantity")
#         self.inventory_tree.heading("Price", text="Price")
#         self.inventory_tree.column("ID", width=80, anchor='center')
#         self.inventory_tree.column("Name", width=230, anchor='w')
#         self.inventory_tree.column("Quantity", width=90, anchor='center')
#         self.inventory_tree.column("Price", width=110, anchor='center')
#         self.inventory_tree.pack(fill='both', expand=True, padx=10, pady=10)

#         self.sales_frame = ttk.Frame(self.notebook, style='TFrame')
#         self.notebook.add(self.sales_frame, text="Sales")

#         # Sales search controls
#         search_frame = ttk.Frame(self.sales_frame, style='TFrame')
#         search_frame.pack(pady=10, padx=10, fill='x')
#         ttk.Label(search_frame, text="Search by ID or Name:", font=("Segoe UI", 11)).pack(side='left', padx=(0,10))
#         self.search_var = tk.StringVar()
#         self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, font=('Segoe UI', 11), width=35)
#         self.search_entry.pack(side='left')
#         search_button = ttk.Button(search_frame, text="Search", command=self.search_items, style='TButton')
#         search_button.pack(side='left', padx=10)
#         clear_button = ttk.Button(search_frame, text="Clear", command=self.clear_search, style='TButton')
#         clear_button.pack(side='left')

#         # Sales items treeview
#         self.sales_tree = ttk.Treeview(self.sales_frame, columns=("ID", "Name", "Quantity", "Price"), show='headings', selectmode='browse')
#         self.sales_tree.heading("ID", text="Item ID")
#         self.sales_tree.heading("Name", text="Name")
#         self.sales_tree.heading("Quantity", text="Available")
#         self.sales_tree.heading("Price", text="Price")
#         self.sales_tree.column("ID", width=80, anchor='center')
#         self.sales_tree.column("Name", width=230, anchor='w')
#         self.sales_tree.column("Quantity", width=90, anchor='center')
#         self.sales_tree.column("Price", width=110, anchor='center')
#         self.sales_tree.pack(fill='both', expand=True, padx=10, pady=5)

#         qty_frame = ttk.Frame(self.sales_frame, style='TFrame')
#         qty_frame.pack(pady=10, padx=10, fill='x')
#         ttk.Label(qty_frame, text="Quantity to sell:", font=("Segoe UI", 11)).pack(side='left', padx=(0,8))
#         self.sell_quantity = ttk.Entry(qty_frame, width=12, font=('Segoe UI', 11))
#         self.sell_quantity.pack(side='left', padx=(0,12))

#         add_to_sale_button = ttk.Button(qty_frame, text="Add to Sale", command=self.add_to_sale, style='Success.TButton')
#         add_to_sale_button.pack(side='left', padx=5)

#         finalize_sale_button = ttk.Button(qty_frame, text="Finalize Sale", command=self.finalize_sale, style='Success.TButton')
#         finalize_sale_button.pack(side='left')

#         # Selected sale items treeview
#         selected_items_label = ttk.Label(self.sales_frame, text="Items Added to Sale:", font=("Segoe UI", 12, 'bold'))
#         selected_items_label.pack(pady=(10, 0), padx=10, anchor='w')

#         self.selected_items_tree = ttk.Treeview(self.sales_frame, columns=("ID", "Name", "Quantity", "Price"), show='headings')
#         self.selected_items_tree.heading("ID", text="Item ID")
#         self.selected_items_tree.heading("Name", text="Name")
#         self.selected_items_tree.heading("Quantity", text="Quantity")
#         self.selected_items_tree.heading("Price", text="Price")
#         self.selected_items_tree.column("ID", width=80, anchor='center')
#         self.selected_items_tree.column("Name", width=230, anchor='w')
#         self.selected_items_tree.column("Quantity", width=90, anchor='center')
#         self.selected_items_tree.column("Price", width=110, anchor='center')
#         self.selected_items_tree.pack(fill='both', expand=True, padx=10, pady=(0,10))

#         remove_item_button = ttk.Button(self.sales_frame, text="Remove Selected Item", command=self.remove_selected_sale_item, style='Danger.TButton')
#         remove_item_button.pack(pady=(0, 10), padx=10, anchor='e')

#         self.status_label = ttk.Label(self.root, text="", foreground="#bb2a2a", font=("Segoe UI", 10, "bold"), background='#f0f4f8')
#         self.status_label.pack(pady=5)

#         self.set_logged_in_state(False)
#         self.refresh_inventory_list()
#         self.refresh_sales_list()

#     def set_logged_in_state(self, logged_in):
#         self.logged_in = logged_in
#         state = 'normal' if logged_in else 'disabled'
#         self.add_button.config(state=state)
#         self.update_button.config(state=state)
#         self.delete_button.config(state=state)
#         self.refresh_inventory_list()
#         self.refresh_sales_list()
#         if not logged_in:
#             self.status_label.config(text="Please log in to access Inventory and Sales.")
#             self.notebook.select(self.login_frame)
#         else:
#             self.status_label.config(text="Logged in as admin.")
#             self.notebook.select(self.home_frame)

#     def handle_login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         if self.admin.verify_login(username, password):
#             self.set_logged_in_state(True)
#             messagebox.showinfo("Success", "Login successful.")
#         else:
#             messagebox.showerror("Error", "Login failed.")

#     def handle_forgot_password(self):
#         username = self.username_entry.get()
#         if not username:
#             messagebox.showwarning("Input Error", "Please enter your username first.")
#             return
#         self.admin.forgot_password(username)

#     def refresh_inventory_list(self):
#         self.inventory_tree.delete(*self.inventory_tree.get_children())
#         for item_id, item in self.inventory.view_inventory().items():
#             self.inventory_tree.insert('', 'end', values=(item_id, item['name'], item['quantity'], f"{item['price']:.2f}"))

#     def refresh_sales_list(self, filtered_items=None):
#         self.sales_tree.delete(*self.sales_tree.get_children())
#         items_to_show = filtered_items if filtered_items is not None else self.inventory.view_inventory()
#         for item_id, item in items_to_show.items():
#             self.sales_tree.insert('', 'end', values=(item_id, item['name'], item['quantity'], f"{item['price']:.2f}"))

#     def show_add_item_dialog(self):
#         if not self.logged_in:
#             messagebox.showerror("Error", "Login required.")
#             return
#         dialog = ItemDialog(self.root, "Add Item")
#         self.root.wait_window(dialog.top)
#         if dialog.result:
#             item_id, name, quantity, price = dialog.result
#             message = self.inventory.add_item(item_id, name, quantity, price)
#             messagebox.showinfo("Add Item", message)
#             self.refresh_inventory_list()
#             self.refresh_sales_list()

#     def show_update_item_options(self):
#         if not self.logged_in:
#             messagebox.showerror("Error", "Login required.")
#             return
#         choice = messagebox.askquestion("Update Item", "Do you want to search for the item to update?\n\nClick 'Yes' for Search, 'No' to select an item from inventory.")
#         if choice == 'yes':
#             self.show_update_item_with_search_dialog()
#         else:
#             self.show_update_item_from_selection()

#     def show_update_item_with_search_dialog(self):
#         UpdateSearchDialog(self.root, self)

#     def show_update_item_from_selection(self):
#         selected = self.inventory_tree.focus()
#         if not selected:
#             messagebox.showwarning("Selection Error", "Please select an item from inventory to update.")
#             return
#         values = self.inventory_tree.item(selected, 'values')
#         self.show_update_item_dialog(values)

#     def show_update_item_dialog(self, values):
#         dialog = ItemDialog(self.root, "Update Item", values)
#         self.root.wait_window(dialog.top)
#         if dialog.result:
#             item_id, name, quantity, price = dialog.result
#             message = self.inventory.update_item(item_id, name, quantity, price)
#             messagebox.showinfo("Update Item", message)
#             self.refresh_inventory_list()
#             self.refresh_sales_list()

#     def delete_selected_item(self):
#         if not self.logged_in:
#             messagebox.showerror("Error", "Login required.")
#             return
#         selected = self.inventory_tree.focus()
#         if not selected:
#             messagebox.showwarning("Selection Error", "Please select an item to delete.")
#             return
#         values = self.inventory_tree.item(selected, 'values')
#         confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete item '{values[1]}'?")
#         if confirm:
#             message = self.inventory.delete_item(values[0])
#             messagebox.showinfo("Delete Item", message)
#             self.refresh_inventory_list()
#             self.refresh_sales_list()

#     def search_items(self):
#         query = self.search_var.get().lower().strip()
#         if not query:
#             messagebox.showwarning("Input Error", "Please enter an ID or name to search.")
#             return
#         filtered = {}
#         for item_id, item in self.inventory.items.items():
#             if query in item_id.lower() or query in item['name'].lower():
#                 filtered[item_id] = item
#         if not filtered:
#             messagebox.showinfo("No results", "No items matched your search.")
#         self.refresh_sales_list(filtered)

#     def clear_search(self):
#         self.search_var.set('')
#         self.refresh_sales_list()

#     def add_to_sale(self):
#         if not self.logged_in:
#             messagebox.showerror("Error", "Login required.")
#             return
#         selected = self.sales_tree.focus()
#         if not selected:
#             messagebox.showwarning("Selection Error", "Please select an item to add to the sale.")
#             return
#         try:
#             qty = int(self.sell_quantity.get())
#             if qty <= 0:
#                 raise ValueError
#         except ValueError:
#             messagebox.showerror("Input Error", "Please enter a valid quantity (positive integer).")
#             return
#         values = self.sales_tree.item(selected, 'values')
#         item_id = values[0]
#         item = self.inventory.items[item_id]
#         if qty > item['quantity']:
#             messagebox.showerror("Error", f"Not enough stock. Available quantity: {item['quantity']}")
#             return

#         # Check if item already in sale list; if so, update quantity
#         for idx, sal_item in enumerate(self.selected_sale_items):
#             if sal_item['item_id'] == item_id:
#                 new_qty = sal_item['quantity'] + qty
#                 if new_qty > item['quantity']:
#                     messagebox.showerror("Error", f"Total quantity in sale exceeds stock. Available: {item['quantity']}")
#                     return
#                 self.selected_sale_items[idx]['quantity'] = new_qty
#                 self.refresh_selected_sale_items()
#                 self.sell_quantity.delete(0, tk.END)
#                 return

#         self.selected_sale_items.append({'item_id': item_id, 'name': item['name'], 'quantity': qty, 'price': item['price']})
#         self.refresh_selected_sale_items()
#         self.sell_quantity.delete(0, tk.END)

#     def refresh_selected_sale_items(self):
#         self.selected_items_tree.delete(*self.selected_items_tree.get_children())
#         for item in self.selected_sale_items:
#             self.selected_items_tree.insert('', 'end', values=(item['item_id'], item['name'], item['quantity'], f"{item['price']:.2f}"))

#     def remove_selected_sale_item(self):
#         selected = self.selected_items_tree.focus()
#         if not selected:
#             messagebox.showwarning("Selection Error", "Please select an item to remove from sale list.")
#             return
#         values = self.selected_items_tree.item(selected, 'values')
#         item_id = values[0]
#         for idx, item in enumerate(self.selected_sale_items):
#             if item['item_id'] == item_id:
#                 del self.selected_sale_items[idx]
#                 break
#         self.refresh_selected_sale_items()

#     def finalize_sale(self):
#         if not self.logged_in:
#             messagebox.showerror("Error", "Login required.")
#             return
#         if not self.selected_sale_items:
#             messagebox.showwarning("Sale Error", "No items added to the sale.")
#             return

#         # Prompt for customer name
#         customer_name = simpledialog.askstring("Customer Name", "Please enter the customer's name:")
#         if not customer_name:
#             messagebox.showwarning("Input Error", "Customer name is required.")
#             return

#         # Verify stock availability
#         for sale_item in self.selected_sale_items:
#             inventory_qty = self.inventory.items[sale_item['item_id']]['quantity']
#             if sale_item['quantity'] > inventory_qty:
#                 messagebox.showerror("Stock Error",
#                                      f"Not enough stock for item {sale_item['name']}. Available: {inventory_qty}")
#                 return

#         total_price = 0
#         receipt_lines = []
#         now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         receipt_lines.append("------ SALES RECEIPT ------")
#         receipt_lines.append(f"Date: {now_str}\n")
#         receipt_lines.append(f"Customer Name: {customer_name}\n")

#         for sale_item in self.selected_sale_items:
#             item_id = sale_item['item_id']
#             qty = sale_item['quantity']
#             price = sale_item['price']
#             total = qty * price
#             total_price += total
#             self.inventory.items[item_id]['quantity'] -= qty
#             self.sales_logger.record_receipt(sale_item['name'], qty, price)
#             self.sales_logger.update_daily_sales(sale_item['name'], qty, total)
#             receipt_lines.append(f"Item: {sale_item['name']}")
#             receipt_lines.append(f"Quantity: {qty}")
#             receipt_lines.append(f"Unit Price: {price:.2f}")
#             receipt_lines.append(f"Total: {total:.2f}\n")

#         receipt_lines.append(f"Grand Total: {total_price:.2f}")
#         receipt_lines.append("\nThank you for your purchase!")

#         self.inventory.save_inventory()
#         self.refresh_inventory_list()
#         self.refresh_sales_list()

#         self.selected_sale_items.clear()
#         self.refresh_selected_sale_items()
#         self.sell_quantity.delete(0, tk.END)

#         receipt_text = '\n'.join(receipt_lines)
#         ReceiptDialog(self.root, receipt_text)

# class ItemDialog:
#     def __init__(self, parent, title, values=None):
#         self.top = tk.Toplevel(parent)
#         self.top.title(title)
#         self.top.geometry("360x280")
#         self.top.resizable(False, False)
#         self.result = None
#         label_id = ttk.Label(self.top, text="Item ID:")
#         label_id.grid(row=0, column=0, padx=15, pady=(20, 5), sticky='e')
#         self.id_entry = ttk.Entry(self.top)
#         self.id_entry.grid(row=0, column=1, padx=15, pady=(20, 5), sticky='we')
#         label_name = ttk.Label(self.top, text="Name:")
#         label_name.grid(row=1, column=0, padx=15, pady=5, sticky='e')
#         self.name_entry = ttk.Entry(self.top)
#         self.name_entry.grid(row=1, column=1, padx=15, pady=5, sticky='we')
#         label_quantity = ttk.Label(self.top, text="Quantity:")
#         label_quantity.grid(row=2, column=0, padx=15, pady=5, sticky='e')
#         self.quantity_entry = ttk.Entry(self.top)
#         self.quantity_entry.grid(row=2, column=1, padx=15, pady=5, sticky='we')
#         label_price = ttk.Label(self.top, text="Price:")
#         label_price.grid(row=3, column=0, padx=15, pady=5, sticky='e')
#         self.price_entry = ttk.Entry(self.top)
#         self.price_entry.grid(row=3, column=1, padx=15, pady=5, sticky='we')
#         btn_frame = ttk.Frame(self.top)
#         btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
#         ok_button = ttk.Button(btn_frame, text="OK", command=self.ok)
#         ok_button.pack(side='left', padx=10)
#         cancel_button = ttk.Button(btn_frame, text="Cancel", command=self.top.destroy)
#         cancel_button.pack(side='left', padx=10)
#         self.top.columnconfigure(1, weight=1)
#         if values:
#             self.id_entry.insert(0, values[0])
#             self.id_entry.config(state='disabled')
#             self.name_entry.insert(0, values[1])
#             self.quantity_entry.insert(0, values[2])
#             self.price_entry.insert(0, values[3])

#     def ok(self):
#         item_id = self.id_entry.get().strip()
#         name = self.name_entry.get().strip()
#         quantity = self.quantity_entry.get().strip()
#         price = self.price_entry.get().strip()
#         if not item_id or not name or not quantity or not price:
#             messagebox.showerror("Input Error", "All fields are required.")
#             return
#         try:
#             quantity = int(quantity)
#             price = float(price)
#             if quantity < 0 or price < 0:
#                 raise ValueError
#         except ValueError:
#             messagebox.showerror("Input Error", "Quantity must be a non-negative integer and Price a non-negative number.")
#             return
#         self.result = (item_id, name, quantity, price)
#         self.top.destroy()

# class ReceiptDialog:
#     def __init__(self, parent, receipt_text):
#         self.top = tk.Toplevel(parent)
#         self.top.title("Sales Receipt")
#         self.top.geometry("400x400")
#         self.top.resizable(False, False)
#         label = ttk.Label(self.top, text="Sales Receipt", font=("Segoe UI", 16, "bold"))
#         label.pack(pady=10)
#         self.text_area = scrolledtext.ScrolledText(self.top, width=48, height=15, font=("Courier New", 11))
#         self.text_area.pack(padx=10, pady=5)
#         self.text_area.insert(tk.END, receipt_text)
#         self.text_area.config(state='disabled')
#         btn_frame = ttk.Frame(self.top)
#         btn_frame.pack(pady=10)
#         save_button = ttk.Button(btn_frame, text="Save Receipt", command=self.save_receipt, style='Success.TButton')
#         save_button.pack(side='left', padx=10)
#         close_button = ttk.Button(btn_frame, text="Close", command=self.top.destroy, style='Danger.TButton')
#         close_button.pack(side='left', padx=10)

#     def save_receipt(self):
#         file_path = filedialog.asksaveasfilename(defaultextension=".txt",
#                                                  filetypes=[("Text Files", "*.txt"), ("PNG Image", "*.png")],
#                                                  title="Save Receipt As")
#         if not file_path:
#             return
#         try:
#             if file_path.lower().endswith('.txt'):
#                 with open(file_path, 'w') as file:
#                     file.write(self.text_area.get('1.0', tk.END))
#                 messagebox.showinfo("Saved", f"Receipt saved as text file:\n{file_path}")
#             elif file_path.lower().endswith('.png'):
#                 self.save_receipt_as_image(file_path)
#                 messagebox.showinfo("Saved", f"Receipt saved as image:\n{file_path}")
#             else:
#                 messagebox.showerror("Error", "Unsupported file extension. Use .txt or .png")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to save receipt:\n{e}")

#     def save_receipt_as_image(self, path):
#         # Create image from the receipt text
#         lines = self.text_area.get('1.0', tk.END).splitlines()
#         font_path = None
#         try:
#             import sys
#             if sys.platform == "win32":
#                 font_path = "C:\\Windows\\Fonts\\consola.ttf"
#             elif sys.platform == "darwin":
#                 font_path = "/System/Library/Fonts/Menlo.ttc"
#             else:
#                 font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
#             font = ImageFont.truetype(font_path, 14)
#         except:
#             font = ImageFont.load_default()
#         max_width = 0
#         line_height = font.getsize('Hg')[1] + 4
#         for line in lines:
#             w, _ = font.getsize(line)
#             if w > max_width:
#                 max_width = w
#         img_height = line_height * len(lines) + 10
#         img_width = max_width + 20
#         image = Image.new("RGB", (img_width, img_height), color="white")
#         draw = ImageDraw.Draw(image)
#         y = 5
#         for line in lines:
#             draw.text((10, y), line, fill="black", font=font)
#             y += line_height
#         image.save(path)

# class UpdateSearchDialog:
#     def __init__(self, parent, pos_app):
#         self.pos_app = pos_app
#         self.top = tk.Toplevel(parent)
#         self.top.title("Search Item to Update")
#         self.top.geometry("400x160")
#         self.top.resizable(False, False)

#         ttk.Label(self.top, text="Search by ID or Name:", font=("Segoe UI", 12)).pack(pady=(20,5))
#         self.search_var = tk.StringVar()
#         self.search_entry = ttk.Entry(self.top, textvariable=self.search_var, font=('Segoe UI', 12))
#         self.search_entry.pack(padx=20, fill='x')
#         self.search_entry.focus()
#         btn_frame = ttk.Frame(self.top)
#         btn_frame.pack(pady=15)
#         search_button = ttk.Button(btn_frame, text="Search", command=self.search, style='Success.TButton')
#         search_button.pack(side='left', padx=10)
#         cancel_button = ttk.Button(btn_frame, text="Cancel", command=self.top.destroy, style='Danger.TButton')
#         cancel_button.pack(side='left', padx=10)

#     def search(self):
#         query = self.search_var.get().lower().strip()
#         if not query:
#             messagebox.showwarning("Input Error", "Please enter an ID or name to search.")
#             return
#         found = None
#         for item_id, item in self.pos_app.inventory.items.items():
#             if query == item_id.lower() or query == item['name'].lower():
#                 found = (item_id, item['name'], str(item['quantity']), f"{item['price']:.2f}")
#                 break
#         if found:
#             self.top.destroy()
#             self.pos_app.show_update_item_dialog(found)
#         else:
#             messagebox.showinfo("No result", "No matching item found.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = POSSystem(root)
#     root.mainloop()

