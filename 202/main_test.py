import unittest

from main import Solution


class TestSolution(unittest.TestCase):
    def test_isHappy(self):
        s = Solution()
        self.assertEqual(s.isHappy(19), True)
        self.assertEqual(s.isHappy(2), False)


if __name__ == '__main__':
    unittest.main()
