class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        if key == root.val:
            if root.left is None and root.right is None:
                return None
            if root.left is not None and root.right is None:
                return root.left
            if root.left is None and root.right is not None:
                return root.right
            if root.right is None:
                raise Exception("impossible")
            cur = root.right
            while cur.left is not None:
                cur = cur.left
            cur.left = root.left
            return root.right
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root
