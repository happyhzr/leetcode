# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)


if __name__ == '__main__':
    s = Solution()

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t2.left = t4
    t2.right = t5
    t6 = TreeNode(4)
    t7 = TreeNode(3)
    t3.left = t6
    t3.right = t7

    print(s.isSymmetric(t1))
