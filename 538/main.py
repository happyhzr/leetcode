class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    previous: TreeNode | None

    def __init__(self) -> None:
        self.previous = None

    def convertBST(self, root: TreeNode | None) -> TreeNode | None:
        self.dfs(root)
        return root

    def dfs(self, current: TreeNode | None) -> None:
        if current is None:
            return None
        self.dfs(current.right)
        if self.previous is not None:
            current.val += self.previous.val
        self.previous = current
        self.dfs(current.left)
