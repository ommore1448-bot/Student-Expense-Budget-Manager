from utils import calculate_percentage


def calculate_total_income(transactions):
    """Calculate total income."""
    total = 0

    for transaction in transactions:
        if transaction["type"].lower() == "income":
            total += transaction["amount"]

    return total


def calculate_total_expenses(transactions):
    """Calculate total expenses."""
    total = 0

    for transaction in transactions:
        if transaction["type"].lower() == "expense":
            total += transaction["amount"]

    return total


def calculate_savings(transactions):
    """Calculate net savings."""
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)

    return total_income - total_expenses


def calculate_savings_percentage(transactions):
    """Calculate savings as a percentage of income."""
    total_income = calculate_total_income(transactions)
    savings = calculate_savings(transactions)

    return calculate_percentage(savings, total_income)


def get_category_totals(transactions):
    """Calculate total expenses for each category."""
    category_totals = {}

    for transaction in transactions:
        if transaction["type"].lower() == "expense":
            category = transaction["category"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += transaction["amount"]

    return category_totals


def get_highest_expense(transactions):
    """Find the transaction with the highest expense amount."""
    expenses = []

    for transaction in transactions:
        if transaction["type"].lower() == "expense":
            expenses.append(transaction)

    if not expenses:
        return None

    highest = expenses[0]

    for transaction in expenses:
        if transaction["amount"] > highest["amount"]:
            highest = transaction

    return highest


def get_lowest_expense(transactions):
    """Find the transaction with the lowest expense amount."""
    expenses = []

    for transaction in transactions:
        if transaction["type"].lower() == "expense":
            expenses.append(transaction)

    if not expenses:
        return None

    lowest = expenses[0]

    for transaction in expenses:
        if transaction["amount"] < lowest["amount"]:
            lowest = transaction

    return lowest


def get_highest_spending_category(transactions):
    """Find the category with the highest total spending."""
    category_totals = get_category_totals(transactions)

    if not category_totals:
        return None

    highest_category = None
    highest_amount = 0

    for category, amount in category_totals.items():
        if amount > highest_amount:
            highest_category = category
            highest_amount = amount

    return highest_category, highest_amount


def display_analysis(transactions):
    """Display a complete financial analysis."""

    if not transactions:
        print("No transactions available for analysis.")
        return

    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    savings = calculate_savings(transactions)
    savings_percentage = calculate_savings_percentage(transactions)

    print("\n" + "=" * 50)
    print("FINANCIAL ANALYSIS".center(50))
    print("=" * 50)

    print(f"Total Income       : {total_income:.2f}")
    print(f"Total Expenses     : {total_expenses:.2f}")
    print(f"Net Savings        : {savings:.2f}")
    print(f"Savings Percentage : {savings_percentage:.2f}%")

    print("\nCategory-wise Expenses")
    print("-" * 50)

    category_totals = get_category_totals(transactions)

    if category_totals:
        for category, amount in category_totals.items():
            print(f"{category:<20} : {amount:.2f}")
    else:
        print("No expenses recorded.")

    highest_expense = get_highest_expense(transactions)

    if highest_expense:
        print("\nHighest Expense")
        print("-" * 50)
        print(f"Category : {highest_expense['category']}")
        print(f"Amount   : {highest_expense['amount']:.2f}")
        print(f"Date     : {highest_expense['date']}")

    lowest_expense = get_lowest_expense(transactions)

    if lowest_expense:
        print("\nLowest Expense")
        print("-" * 50)
        print(f"Category : {lowest_expense['category']}")
        print(f"Amount   : {lowest_expense['amount']:.2f}")
        print(f"Date     : {lowest_expense['date']}")

    highest_category = get_highest_spending_category(transactions)

    if highest_category:
        category, amount = highest_category

        print("\nHighest Spending Category")
        print("-" * 50)
        print(f"Category : {category}")
        print(f"Amount   : {amount:.2f}")

    print("=" * 50)