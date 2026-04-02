class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        left = self.hasPathSum(root.left, targetSum - root.val)
        if left:
            return left
        return self.hasPathSum(root.right, targetSum - root.val)
