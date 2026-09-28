import unittest

from budget_manager import (
    calculate_total_expenses,
    calculate_remaining_budget,
    calculate_budget_percentage,
    get_budget_status
)


class TestBudget(unittest.TestCase):

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
            }
        ]

    def test_total_expenses(self):
        self.assertEqual(
            calculate_total_expenses(self.transactions),
            1000.0
        )

    def test_remaining_budget(self):
        self.assertEqual(
            calculate_remaining_budget(5000, self.transactions),
            4000.0
        )

    def test_budget_percentage(self):
        self.assertEqual(
            calculate_budget_percentage(5000, self.transactions),
            20.0
        )

    def test_budget_status_within_budget(self):
        self.assertEqual(
            get_budget_status(5000, self.transactions),
            "Within Budget"
        )

    def test_budget_status_almost_exceeded(self):
        self.assertEqual(
            get_budget_status(1200, self.transactions),
            "Budget Almost Exceeded"
        )

    def test_budget_status_exceeded(self):
        self.assertEqual(
            get_budget_status(500, self.transactions),
            "Budget Exceeded"
        )


if __name__ == "__main__":
    unittest.main()