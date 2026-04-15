class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev: TreeNode | None

    def __init__(self) -> None:
        self.prev = None

    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        left = self.isValidBST(root.left)
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        right = self.isValidBST(root.right)
        return left and right
