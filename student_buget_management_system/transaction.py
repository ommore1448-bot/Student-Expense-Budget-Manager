def create_transaction(transaction_id, date, transaction_type, category, amount, description):
    """Create and return a transaction dictionary."""
    transaction = {
        "id": transaction_id,
        "date": date,
        "type": transaction_type,
        "category": category,
        "amount": float(amount),
        "description": description
    }

    return transaction


def display_transaction(transaction):
    """Display one transaction in a readable format."""
    print("\n------------------------------")
    print("Transaction ID :", transaction["id"])
    print("Date           :", transaction["date"])
    print("Type           :", transaction["type"])
    print("Category       :", transaction["category"])
    print("Amount         :", transaction["amount"])
    print("Description    :", transaction["description"])
    print("------------------------------")


def get_transaction_type(transaction):
    """Return the transaction type."""
    return transaction["type"]


def get_transaction_amount(transaction):
    """Return the transaction amount."""
    return transaction["amount"]