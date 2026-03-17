class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        if root.left and not root.right:
            return False
        if not root.left and root.right:
            return False
        return self.helper(root.left, root.right)

    def helper(self, left: TreeNode | None, right: TreeNode | None):
        if not left and not right:
            return True
        if left and not right:
            return False
        if not left and right:
            return False
        if not left or not right:
            raise Exception("impossible")
        if left.val != right.val:
            return False
        outside = self.helper(left.left, right.right)
        inside = self.helper(left.right, right.left)
        return outside and inside
