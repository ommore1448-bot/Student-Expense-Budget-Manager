import unittest

from transaction import create_transaction
from validators import (
    validate_amount,
    validate_date,
    validate_category,
    validate_description,
    validate_transaction_type
)


class TestTransactions(unittest.TestCase):

    def test_create_transaction(self):
        transaction = create_transaction(
            1,
            "27-09-2026",
            "Expense",
            "Food",
            150,
            "Lunch"
        )

        self.assertEqual(transaction["id"], 1)
        self.assertEqual(transaction["date"], "27-09-2026")
        self.assertEqual(transaction["type"], "Expense")
        self.assertEqual(transaction["category"], "Food")
        self.assertEqual(transaction["amount"], 150.0)
        self.assertEqual(transaction["description"], "Lunch")

    def test_valid_amount(self):
        self.assertTrue(validate_amount("150"))

    def test_invalid_amount(self):
        self.assertFalse(validate_amount("abc"))
        self.assertFalse(validate_amount("-100"))
        self.assertFalse(validate_amount("0"))

    def test_valid_transaction_type(self):
        self.assertTrue(validate_transaction_type("Income"))
        self.assertTrue(validate_transaction_type("Expense"))

    def test_invalid_transaction_type(self):
        self.assertFalse(validate_transaction_type("Savings"))

    def test_valid_date(self):
        self.assertTrue(validate_date("27-09-2026"))

    def test_invalid_date_format(self):
        self.assertFalse(validate_date("2026-09-27"))
        self.assertFalse(validate_date("27/09/2026"))

    def test_category_validation(self):
        self.assertTrue(validate_category("Food"))
        self.assertFalse(validate_category(""))

    def test_description_validation(self):
        self.assertTrue(validate_description("Lunch"))
        self.assertFalse(validate_description(""))


if __name__ == "__main__":
    unittest.main()