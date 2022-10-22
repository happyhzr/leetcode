import unittest

from main import Solution


class TestSolution(unittest.TestCase):
    def test_removeElements(self):
        s = Solution()
        head = s.new_list([1, 2, 3, 4, 5, 6])
        head = s.removeElements(head, 6)
        self.assertEqual(s.get_list(head), [1, 2, 3, 4, 5])
        head = s.new_list([])
        head = s.removeElements(head, 1)
        self.assertEqual(s.get_list(head), [])
        head = s.new_list([7, 7, 7, 7])
        head = s.removeElements(head, 7)
        self.assertEqual(s.get_list(head), [])


if __name__ == '__main__':
    unittest.main()
