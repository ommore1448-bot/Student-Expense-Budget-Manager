import csv
import os


def save_transactions(transactions, filename="data/expenses.csv"):
    """Save transactions to a CSV file."""
    directory = os.path.dirname(filename)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "id",
            "date",
            "type",
            "category",
            "amount",
            "description"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for transaction in transactions:
            writer.writerow(transaction)


def load_transactions(filename="data/expenses.csv"):
    """Load transactions from a CSV file."""
    transactions = []

    if not os.path.exists(filename):
        return transactions

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    transaction = {
                        "id": int(row["id"]),
                        "date": row["date"],
                        "type": row["type"],
                        "category": row["category"],
                        "amount": float(row["amount"]),
                        "description": row["description"]
                    }

                    transactions.append(transaction)

                except (ValueError, KeyError, TypeError):
                    print("Warning: Invalid transaction record skipped.")

    except (OSError, csv.Error):
        print("Warning: Unable to read transaction data.")

    return transactions