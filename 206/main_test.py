import unittest

from main import Solution


class TestSolution(unittest.TestCase):
    def test_reverseList(self):
        s = Solution()
        head = s.new_list([1, 2, 3, 4, 5])
        head = s.reverseList(head)
        print(s.get_list(head))

        head = s.new_list([1, 2])
        head = s.reverseList(head)
        print(s.get_list(head))

        head = s.new_list([])
        head = s.reverseList(head)
        print(s.get_list(head))


if __name__ == '__main__':
    unittest.main()
