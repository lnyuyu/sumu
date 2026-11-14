import unittest

from names import normalize_name
from reports import old_report


class ReportTests(unittest.TestCase):
    def test_normalize_strips_and_casefolds(self):
        self.assertEqual(normalize_name("  Straße "), "strasse")

    def test_old_report_merges_variants(self):
        rows = [{"name": " Straße "}, {"name": "STRASSE"}]
        self.assertEqual(old_report(rows), {"strasse": 2})


if __name__ == "__main__":
    unittest.main()