# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p) and (not q):
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False


if __name__ == '__main__':
    s = Solution()

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    print(s.isSameTree(t1, t1))

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t1.left = t2
    t3 = TreeNode(1)
    t4 = TreeNode(2)
    t3.right = t4
    print(s.isSameTree(t1, t3))

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(2)
    t4.left = t5
    t4.right = t6
    print(s.isSameTree(t1, t4))
