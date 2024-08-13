Overview
This project is a comprehensive Grocery Store Management System developed as part of an assignment. The system is designed to manage various aspects of a grocery store's operations, including inventory management, user authentication, and transaction processing. The program is built using C programming language and adheres to the Object-Oriented Programming (OOP) principles and practices.

Features
User Roles
Admin
Add new items to the inventory.
Update item details (e.g., code, description, category, unit, price, quantity, minimum).
Delete items from the inventory.
Perform stock-taking operations.
View and manage the replenishment list.
Replenish stock quantities.
Search for items using various criteria (description, code range, category, price range).
Add new user accounts with encrypted passwords.
Inventory Checker
Perform stock-taking operations.
Search for items using various criteria.
Purchaser
View the replenishment list.
Replenish stock quantities.
Search for items using various criteria.
Key Functionalities
User Authentication: Secure login system that verifies credentials and grants access based on user roles.
Inventory Management: Functions to add, update, delete, and search for items in the store's inventory.
Stock Management: Track and manage stock levels, including viewing and updating quantities based on replenishment needs.
Data Security: Passwords are encrypted using a custom encryption algorithm to protect user data.
System Design
The project follows a structured approach, including pseudocode and flowcharts for each function to outline the operations and logic before implementation. This ensures that the system is robust, maintainable, and easy to understand.

Key Functions
INSERT_ITEM: Adds new items to the inventory.
UPDATE_ITEM: Updates existing item details.
DELETE_ITEM: Removes items from the inventory.
STOCK_TAKING: Confirms or updates the quantity of items in stock.
VIEW_REPLENISH_LIST: Displays items that need to be replenished.
STOCK_REPLENISHMENT: Updates the quantity of items after replenishment.
USER_AUTHENTICATION: Validates user credentials and manages access rights.
ENCRYPT_PASS: Encrypts user passwords for secure storage.
DECRYPT_PASS: Decrypts passwords during the login process for validation.
DISPLAY: Shows the current inventory list.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/grocery-store-management-system.git
Compile the code using a C compiler:
bash
Copy code
gcc -o grocery_system main.c
Run the program:
bash
Copy code
./grocery_system
Usage
Admin: Manages all aspects of the grocery store's inventory and user accounts.
Inventory Checker: Handles stock-taking and searching for items.
Purchaser: Manages the replenishment of stock based on the system's recommendations.
Testing
The program has been thoroughly tested to ensure that all functionalities work as expected. Testing includes adding, updating, deleting items, performing stock-taking, viewing the replenishment list, and validating the user authentication process.

Conclusion
This Grocery Store Management System is a robust and user-friendly tool designed to manage the day-to-day operations of a grocery store efficiently. The system adheres to best practices in programming, with a focus on data integrity, security, and maintainability.

License
This project is licensed under the MIT License - see the LICENSE file for details.
