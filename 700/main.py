class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return root
        if root.val == val:
            return root
        node: TreeNode | None = None
        if val < root.val:
            node = self.searchBST(root.left, val)
        elif val > root.val:
            node = self.searchBST(root.right, val)
        return node
