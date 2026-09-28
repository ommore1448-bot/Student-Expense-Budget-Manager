def generate_transaction_id(transactions):
    """Generate the next transaction ID."""
    if not transactions:
        return 1

    highest_id = 0

    for transaction in transactions:
        if transaction["id"] > highest_id:
            highest_id = transaction["id"]

    return highest_id + 1


def format_amount(amount):
    """Format an amount to two decimal places."""
    return f"{amount:.2f}"


def print_heading(title):
    """Print a formatted heading."""
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def print_separator():
    """Print a separator line."""
    print("-" * 50)


def calculate_percentage(value, total):
    """Calculate percentage safely."""
    if total == 0:
        return 0

    return (value / total) * 100