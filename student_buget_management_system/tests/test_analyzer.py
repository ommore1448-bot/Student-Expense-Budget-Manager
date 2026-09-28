import unittest

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


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {
                "id": 1,
                "date": "27-09-2026",
                "type": "Income",
                "category": "Allowance",
                "amount": 10000.0,
                "description": "Monthly allowance"
            },
            {
                "id": 2,
                "date": "27-09-2026",
                "type": "Expense",
                "category": "Food",
                "amount": 150.0,
                "description": "Lunch"
            },
            {
                "id": 3,
                "date": "27-09-2026",
                "type": "Expense",
                "category": "Travel",
                "amount": 850.0,
                "description": "Bus pass"
            },
            {
                "id": 4,
                "date": "27-09-2026",
                "type": "Expense",
                "category": "Food",
                "amount": 200.0,
                "description": "Snacks"
            }
        ]

    def test_total_income(self):
        self.assertEqual(
            calculate_total_income(self.transactions),
            10000.0
        )

    def test_total_expenses(self):
        self.assertEqual(
            calculate_total_expenses(self.transactions),
            1200.0
        )

    def test_savings(self):
        self.assertEqual(
            calculate_savings(self.transactions),
            8800.0
        )

    def test_savings_percentage(self):
        self.assertEqual(
            calculate_savings_percentage(self.transactions),
            88.0
        )

    def test_category_totals(self):
        category_totals = get_category_totals(self.transactions)

        self.assertEqual(category_totals["Food"], 350.0)
        self.assertEqual(category_totals["Travel"], 850.0)

    def test_highest_expense(self):
        highest = get_highest_expense(self.transactions)

        self.assertEqual(highest["amount"], 850.0)
        self.assertEqual(highest["category"], "Travel")

    def test_lowest_expense(self):
        lowest = get_lowest_expense(self.transactions)

        self.assertEqual(lowest["amount"], 150.0)
        self.assertEqual(lowest["category"], "Food")

    def test_highest_spending_category(self):
        category, amount = get_highest_spending_category(
            self.transactions
        )

        self.assertEqual(category, "Travel")
        self.assertEqual(amount, 850.0)


if __name__ == "__main__":
    unittest.main()