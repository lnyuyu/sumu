import unittest
from contextlib import contextmanager

from bank import PermissionDenied, transfer


class FakeDb:
    def __init__(self, allowed=True, fail_credit=False):
        self.allowed = allowed
        self.fail_credit = fail_credit
        self.balances = {"a": 100, "b": 0}
        self.rolled_back = False

    def can_operate(self, user, account):
        return self.allowed

    @contextmanager
    def transaction(self):
        snapshot = dict(self.balances)
        try:
            yield
        except Exception:
            self.balances = snapshot
            self.rolled_back = True
            raise

    def debit(self, account, amount):
        self.balances[account] -= amount

    def credit(self, account, amount):
        if self.fail_credit:
            raise RuntimeError("credit failed")
        self.balances[account] += amount


class TransferTests(unittest.TestCase):
    def test_moves_money(self):
        db = FakeDb()
        transfer(db, "u", "a", "b", 30)
        self.assertEqual(db.balances, {"a": 70, "b": 30})

    def test_rejects_bad_amount(self):
        for amount in (0, -5, 1.5, "10"):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                transfer(FakeDb(), "u", "a", "b", amount)

    def test_rejects_unauthorized_user(self):
        with self.assertRaises(PermissionDenied):
            transfer(FakeDb(allowed=False), "u", "a", "b", 10)

    def test_rolls_back_and_propagates(self):
        db = FakeDb(fail_credit=True)
        with self.assertRaisesRegex(RuntimeError, "credit failed"):
            transfer(db, "u", "a", "b", 10)
        self.assertTrue(db.rolled_back)
        self.assertEqual(db.balances, {"a": 100, "b": 0})


if __name__ == "__main__":
    unittest.main()