class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int
    prev: TreeNode | None

    def __init__(self) -> None:
        self.result = 0
        self.prev = None

    def getMinimumDifference(self, root: TreeNode | None) -> int:
        self.result = 10**5
        self.prev = None
        self.dfs(root)
        return self.result

    def dfs(self, curr: TreeNode | None) -> None:
        if not curr:
            return
        self.dfs(curr.left)
        if self.prev:
            self.result = min(self.result, abs(curr.val - self.prev.val))
        self.prev = curr
        self.dfs(curr.right)
