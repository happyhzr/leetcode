class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.depth(root) != -1

    def depth(self, node: TreeNode | None) -> int:
        if not node:
            return 0
        left = self.depth(node.left)
        if left == -1:
            return -1
        right = self.depth(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
