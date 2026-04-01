class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth: int
    result: int

    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        self.max_depth = -1
        self.dfs(root, 0)
        return self.result

    def dfs(self, node: TreeNode | None, depth: int) -> None:
        if not node:
            return
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
