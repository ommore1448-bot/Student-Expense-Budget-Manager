from analyzer import (
    calculate_total_income,
    calculate_total_expenses,
    calculate_savings,
    calculate_savings_percentage,
    get_category_totals,
    get_highest_expense,
    get_lowest_expense,
    get_highest_spending_category
)
from budget_manager import (
    calculate_remaining_budget,
    calculate_budget_percentage,
    get_budget_status
)


def generate_report(transactions, budget):
    """Generate a complete financial report."""

    if not transactions:
        print("\nNo transactions available.")
        return

    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    savings = calculate_savings(transactions)
    savings_percentage = calculate_savings_percentage(transactions)

    remaining_budget = calculate_remaining_budget(
        budget,
        transactions
    )

    budget_percentage = calculate_budget_percentage(
        budget,
        transactions
    )

    budget_status = get_budget_status(
        budget,
        transactions
    )

    print("\n")
    print("=" * 60)
    print("STUDENT FINANCIAL REPORT".center(60))
    print("=" * 60)

    print("\nFINANCIAL SUMMARY")
    print("-" * 60)
    print(f"Total Income       : {total_income:.2f}")
    print(f"Total Expenses     : {total_expenses:.2f}")
    print(f"Net Savings        : {savings:.2f}")
    print(f"Savings Percentage : {savings_percentage:.2f}%")

    print("\nBUDGET SUMMARY")
    print("-" * 60)
    print(f"Monthly Budget     : {budget:.2f}")
    print(f"Remaining Budget   : {remaining_budget:.2f}")
    print(f"Budget Used        : {budget_percentage:.2f}%")
    print(f"Budget Status      : {budget_status}")

    print("\nCATEGORY-WISE EXPENSES")
    print("-" * 60)

    category_totals = get_category_totals(transactions)

    if category_totals:
        for category, amount in category_totals.items():
            print(f"{category:<25} : {amount:.2f}")
    else:
        print("No expenses recorded.")

    highest_expense = get_highest_expense(transactions)

    if highest_expense:
        print("\nHIGHEST EXPENSE")
        print("-" * 60)
        print(f"Category    : {highest_expense['category']}")
        print(f"Amount      : {highest_expense['amount']:.2f}")
        print(f"Date        : {highest_expense['date']}")
        print(f"Description : {highest_expense['description']}")

    lowest_expense = get_lowest_expense(transactions)

    if lowest_expense:
        print("\nLOWEST EXPENSE")
        print("-" * 60)
        print(f"Category    : {lowest_expense['category']}")
        print(f"Amount      : {lowest_expense['amount']:.2f}")
        print(f"Date        : {lowest_expense['date']}")
        print(f"Description : {lowest_expense['description']}")

    highest_category = get_highest_spending_category(transactions)

    if highest_category:
        category, amount = highest_category

        print("\nHIGHEST SPENDING CATEGORY")
        print("-" * 60)
        print(f"Category : {category}")
        print(f"Amount   : {amount:.2f}")

    print("\n" + "=" * 60)
    print("End of Report".center(60))
    print("=" * 60)