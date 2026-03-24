class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + min(left, right)
