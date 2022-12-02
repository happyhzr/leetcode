import unittest

from main import Solution


class TestSolution(unittest.TestCase):
    def test_addDigits(self):
        s = Solution()
        self.assertEqual(s.addDigits(38), 2)
        self.assertEqual(s.addDigits(0), 0)


if __name__ == '__main__':
    unittest.main()
