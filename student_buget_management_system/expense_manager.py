from transaction import create_transaction
from utils import generate_transaction_id
from validators import (
    validate_amount,
    validate_category,
    validate_date,
    validate_description,
    validate_transaction_type
)


def add_transaction(transactions, transaction_type):
    """Add a new income or expense transaction."""

    while True:
        date = input("Enter date (DD-MM-YYYY): ")

        if validate_date(date):
            break

        print("Invalid date. Please use DD-MM-YYYY format.")

    while True:
        category = input("Enter category: ").strip()

        if validate_category(category):
            break

        print("Category cannot be empty.")

    while True:
        amount = input("Enter amount: ")

        if validate_amount(amount):
            amount = float(amount)
            break

        print("Invalid amount. Enter a positive number.")

    while True:
        description = input("Enter description: ").strip()

        if validate_description(description):
            break

        print("Description cannot be empty.")

    transaction_id = generate_transaction_id(transactions)

    transaction = create_transaction(
        transaction_id,
        date,
        transaction_type,
        category,
        amount,
        description
    )

    transactions.append(transaction)

    print(f"{transaction_type} added successfully.")


def view_transactions(transactions):
    """Display all transactions."""

    if not transactions:
        print("No transactions found.")
        return

    print("\nAll Transactions")

    for transaction in transactions:
        print("-" * 50)
        print("ID          :", transaction["id"])
        print("Date        :", transaction["date"])
        print("Type        :", transaction["type"])
        print("Category    :", transaction["category"])
        print("Amount      :", f"{transaction['amount']:.2f}")
        print("Description :", transaction["description"])


def search_transactions(transactions):
    """Search transactions by date, category, or type."""

    if not transactions:
        print("No transactions found.")
        return

    print("\nSearch Transactions")
    print("1. Search by date")
    print("2. Search by category")
    print("3. Search by type")

    choice = input("Enter choice: ")

    found = []

    if choice == "1":
        search_value = input("Enter date (DD-MM-YYYY): ").strip()

        for transaction in transactions:
            if transaction["date"] == search_value:
                found.append(transaction)

    elif choice == "2":
        search_value = input("Enter category: ").strip().lower()

        for transaction in transactions:
            if transaction["category"].lower() == search_value:
                found.append(transaction)

    elif choice == "3":
        search_value = input("Enter type (Income/Expense): ").strip().lower()

        for transaction in transactions:
            if transaction["type"].lower() == search_value:
                found.append(transaction)

    else:
        print("Invalid choice.")
        return

    if not found:
        print("No matching transactions found.")
        return

    print("\nMatching Transactions")

    for transaction in found:
        print("-" * 50)
        print("ID          :", transaction["id"])
        print("Date        :", transaction["date"])
        print("Type        :", transaction["type"])
        print("Category    :", transaction["category"])
        print("Amount      :", f"{transaction['amount']:.2f}")
        print("Description :", transaction["description"])


def find_transaction_by_id(transactions, transaction_id):
    """Find a transaction using its ID."""

    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction

    return None


def edit_transaction(transactions):
    """Edit an existing transaction."""

    if not transactions:
        print("No transactions found.")
        return

    try:
        transaction_id = int(input("Enter transaction ID to edit: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    transaction = find_transaction_by_id(transactions, transaction_id)

    if transaction is None:
        print("Transaction not found.")
        return

    print("\nWhat do you want to change?")
    print("1. Date")
    print("2. Type")
    print("3. Category")
    print("4. Amount")
    print("5. Description")

    choice = input("Enter choice: ")

    if choice == "1":
        new_date = input("Enter new date (DD-MM-YYYY): ")

        if validate_date(new_date):
            transaction["date"] = new_date
            print("Date updated successfully.")
        else:
            print("Invalid date.")

    elif choice == "2":
        new_type = input("Enter new type (Income/Expense): ").strip().lower()

        if validate_transaction_type(new_type):
            transaction["type"] = new_type.capitalize()
            print("Type updated successfully.")
        else:
            print("Invalid type.")

    elif choice == "3":
        new_category = input("Enter new category: ").strip()

        if validate_category(new_category):
            transaction["category"] = new_category
            print("Category updated successfully.")
        else:
            print("Category cannot be empty.")

    elif choice == "4":
        new_amount = input("Enter new amount: ")

        if validate_amount(new_amount):
            transaction["amount"] = float(new_amount)
            print("Amount updated successfully.")
        else:
            print("Invalid amount.")

    elif choice == "5":
        new_description = input("Enter new description: ").strip()

        if validate_description(new_description):
            transaction["description"] = new_description
            print("Description updated successfully.")
        else:
            print("Description cannot be empty.")

    else:
        print("Invalid choice.")


def delete_transaction(transactions):
    """Delete a transaction using its ID."""

    if not transactions:
        print("No transactions found.")
        return

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid transaction ID.")
        return

    transaction = find_transaction_by_id(transactions, transaction_id)

    if transaction is None:
        print("Transaction not found.")
        return

    transactions.remove(transaction)

    print("Transaction deleted successfully.")