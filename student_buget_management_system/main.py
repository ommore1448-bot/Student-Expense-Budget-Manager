from expense_manager import (
    add_transaction,
    view_transactions,
    search_transactions,
    edit_transaction,
    delete_transaction
)
from file_manager import load_transactions, save_transactions
from budget_manager import set_budget, display_budget_summary
from analyzer import display_analysis
from report import generate_report


def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 55)
    print("STUDENT EXPENSE & BUDGET MANAGEMENT SYSTEM".center(55))
    print("=" * 55)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Search Transactions")
    print("5. Edit Transaction")
    print("6. Delete Transaction")
    print("7. Set Monthly Budget")
    print("8. View Budget Status")
    print("9. Financial Analysis")
    print("10. Generate Financial Report")
    print("11. Save Data")
    print("12. Exit")

    print("=" * 55)


def main():
    """Run the Student Expense & Budget Management System."""

    transactions = load_transactions()
    budget = 0

    print("\nWelcome to Student Expense & Budget Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n--- Add Income ---")
            add_transaction(transactions , "Income")

        elif choice == "2":
            print("\n--- Add Expense ---")
            add_transaction(transactions , "Expense")

            # Change the transaction type if the user selected expense.
            # The add_transaction function already handles both types.

        elif choice == "3":
            print("\n--- View Transactions ---")
            view_transactions(transactions)

        elif choice == "4":
            print("\n--- Search Transactions ---")
            search_transactions(transactions)

        elif choice == "5":
            print("\n--- Edit Transaction ---")
            edit_transaction(transactions)

        elif choice == "6":
            print("\n--- Delete Transaction ---")
            delete_transaction(transactions)

        elif choice == "7":
            print("\n--- Set Monthly Budget ---")
            budget = set_budget()
            print(f"Monthly budget set to {budget:.2f}")

        elif choice == "8":
            print("\n--- Budget Status ---")

            if budget <= 0:
                print("Please set a monthly budget first.")
            else:
                display_budget_summary(budget, transactions)

        elif choice == "9":
            print("\n--- Financial Analysis ---")
            display_analysis(transactions)

        elif choice == "10":
            print("\n--- Financial Report ---")

            if budget <= 0:
                print("Please set a monthly budget before generating the report.")
            else:
                generate_report(transactions, budget)

        elif choice == "11":
            save_transactions(transactions)
            print("Data saved successfully.")

        elif choice == "12":
            save_transactions(transactions)
            print("Data saved successfully.")
            print("Thank you for using the Student Expense & Budget Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 12.")


if __name__ == "__main__":
    main()