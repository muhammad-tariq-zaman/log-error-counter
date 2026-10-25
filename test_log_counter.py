import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from log_counter import count_errors
class T(unittest.TestCase):
    def test_counts(self):
        c = count_errors("INFO ok\nERROR failed\nERROR again\nWARNING slow\n")
        self.assertEqual(c, {"ERROR": 2, "WARNING": 1})
    def test_empty(self):
        self.assertEqual(count_errors("all fine\n"), {})
if __name__ == "__main__": unittest.main()
