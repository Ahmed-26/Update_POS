# Point of Sale (POS) System

## 📚 Contents

- [Point of Sale (POS) System](#point-of-sale-pos-system)
  - [📚 Contents](#-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
    - [Usage](#usage)
    - [Code Structure](#code-structure)
    - [File Structure](#file-structure)

---

## Overview

The Point of Sale (POS) System is a comprehensive application developed in Python using the Tkinter library for the graphical user interface. This system allows administrators to manage inventory, process sales, and generate receipts efficiently.

## Features

- **Admin Management**:

  - Admin login functionality with username and password.
  - Password recovery through security questions.

- **Inventory Management**:

  - Add, update, delete, and view inventory items.
  - Inventory data is stored in a text file.

- **Sales Processing**:

  - Add items to a sale and finalize transactions.
  - Generate and display sales receipts.

- **User Interface**:

  - Intuitive GUI with multiple tabs for Home, Admin Login, Inventory Management, and Sales.
  - Responsive design with a modern look and feel.

- **Receipt Generation**:
  - Sales receipts can be displayed and saved in both text and image formats.

## Installation

1. Ensure you have Python installed on your machine.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

Clone the repository or download the code files.

### Usage

1. Run the application:
   ```bash
   streamlit run main.py
   ```
2. Log in using the default credentials:
   - Username: admin
   - Password: password

3.Navigate through the tabs to manage inventory and process sales.

### Code Structure

- **Admin Class:** Handles admin data loading, login verification, and password recovery.
- **Inventory Class:** Manages inventory items, including loading, saving, and modifying item data.
- **SalesLogger Class:** Records sales transactions and updates daily sales logs.
- **POSSystem Class:** Main application class that initializes the GUI and handles user interactions.
- **ItemDialog Class:** Dialog for adding and updating inventory items.
- **ReceiptDialog Class:** Displays the sales receipt and provides options to save it.
- **UpdateSearchDialog Class:** Facilitates searching for items to update in the inventory.

### File Structure

    ├── pos_system.py          # Main application file
    ├── database.txt           # Inventory data file
    ├── admin_data.txt         # Admin credentials file
    ├── sales_receipt.txt      # Sales receipt log
    ├── daily_sales.txt        # Daily sales log
    └── logo.png               # Application logo

For any inquiries or collaborations, feel free to reach out:

**LinkedIn**: [Ahmed Rasheed](https://www.linkedin.com/in/ahmed-rasheed-7123701b6/)\
 **Email**: [ahmedrasheed6008@gmail.com](mailto:ahmedrasheed6008@gmail.com)
