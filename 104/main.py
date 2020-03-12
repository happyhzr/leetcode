# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r)+1


if __name__ == '__main__':
    s = Solution()

    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t3.left = t4
    t3.right = t5
    print(s.maxDepth(t1))
