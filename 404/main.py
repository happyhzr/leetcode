class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        if not root.left:
            left = 0
        elif not root.left.left and not root.left.right:
            left = root.left.val
        right = self.sumOfLeftLeaves(root.right)
        return left + right
