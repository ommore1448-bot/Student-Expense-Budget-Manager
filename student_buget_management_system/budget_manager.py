def set_budget():
    """Ask the user to enter a monthly budget."""
    while True:
        try:
            budget = float(input("Enter monthly budget: "))

            if budget > 0:
                return budget

            print("Budget must be greater than zero.")

        except ValueError:
            print("Invalid amount. Please enter a number.")


def calculate_total_expenses(transactions):
    """Calculate total expenses."""
    total = 0

    for transaction in transactions:
        if transaction["type"].lower() == "expense":
            total += transaction["amount"]

    return total


def calculate_remaining_budget(budget, transactions):
    """Calculate the amount remaining from the budget."""
    total_expenses = calculate_total_expenses(transactions)

    return budget - total_expenses


def calculate_budget_percentage(budget, transactions):
    """Calculate the percentage of budget already used."""
    if budget <= 0:
        return 0

    total_expenses = calculate_total_expenses(transactions)

    return (total_expenses / budget) * 100


def get_budget_status(budget, transactions):
    """Return the current budget status."""

    remaining = calculate_remaining_budget(budget, transactions)
    percentage = calculate_budget_percentage(budget, transactions)

    if remaining < 0:
        return "Budget Exceeded"

    elif percentage >= 80:
        return "Budget Almost Exceeded"

    else:
        return "Within Budget"


def display_budget_summary(budget, transactions):
    """Display a summary of the current budget."""

    total_expenses = calculate_total_expenses(transactions)
    remaining = calculate_remaining_budget(budget, transactions)
    percentage = calculate_budget_percentage(budget, transactions)
    status = get_budget_status(budget, transactions)

    print("\n" + "=" * 50)
    print("BUDGET SUMMARY".center(50))
    print("=" * 50)

    print(f"Monthly Budget     : {budget:.2f}")
    print(f"Total Expenses     : {total_expenses:.2f}")
    print(f"Remaining Budget   : {remaining:.2f}")
    print(f"Budget Used        : {percentage:.2f}%")
    print(f"Budget Status      : {status}")

    print("=" * 50)