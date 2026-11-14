import unittest

from orders import save_order


class FakeConn:
    def __init__(self, fail=False):
        self.fail = fail
        self.log = []

    def begin(self):
        self.log.append("begin")

    def insert(self, table, row):
        if self.fail:
            raise RuntimeError("disk full")
        self.log.append("insert")
        return 1

    def commit(self):
        self.log.append("commit")

    def rollback(self):
        self.log.append("rollback")

    def release(self):
        self.log.append("release")


class SaveOrderTests(unittest.TestCase):
    def test_commit_then_release(self):
        conn = FakeConn()
        self.assertEqual(save_order(conn, {"id": 1}), 1)
        self.assertEqual(conn.log, ["begin", "insert", "commit", "release"])

    def test_rollback_and_reraise(self):
        conn = FakeConn(fail=True)
        with self.assertRaises(RuntimeError):
            save_order(conn, {"id": 1})
        self.assertEqual(conn.log, ["begin", "rollback", "release"])


if __name__ == "__main__":
    unittest.main()