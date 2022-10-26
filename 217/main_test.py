import unittest

from main import Solution


class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        s = Solution()
        print(s.containsDuplicate([1, 2, 3, 1]))
        print(s.containsDuplicate([1, 2, 3, 4]))
        print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    unittest.main()
