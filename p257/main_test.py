import unittest

from main import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_binaryTreePaths(self):
        s = Solution()
        t1 = TreeNode(1)
        t2 = TreeNode(2)
        t3 = TreeNode(3)
        t4 = TreeNode(5)
        t1.left = t2
        t1.right = t3
        t2.right = t4
        self.assertEqual(s.binaryTreePaths(t1), ['1->2->5', '1->3'])

        t1 = TreeNode(1)
        self.assertEqual(s.binaryTreePaths(t1), ['1'])


if __name__ == '__main__':
    unittest.main()
