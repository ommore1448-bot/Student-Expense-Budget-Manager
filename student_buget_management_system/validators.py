def validate_amount(amount):
    """Validate that an amount is a positive number."""
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_transaction_type(transaction_type):
    """Validate transaction type."""
    transaction_type = transaction_type.strip().lower()

    return transaction_type in ["income", "expense"]


def validate_date(date):
    """Validate date in DD-MM-YYYY format."""
    parts = date.strip().split("-")

    if len(parts) != 3:
        return False

    day, month, year = parts

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    if year < 1:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    return True


def validate_category(category):
    """Validate that category is not empty."""
    return bool(category.strip())


def validate_description(description):
    """Validate that description is not empty."""
    return bool(description.strip())


def validate_menu_choice(choice, minimum, maximum):
    """Validate a menu choice within a given range."""
    try:
        choice = int(choice)

        return minimum <= choice <= maximum

    except ValueError:
        return False