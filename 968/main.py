# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int

    def __init__(self) -> None:
        self.result = 0

    def minCameraCover(self, root: TreeNode | None) -> int:
        status = self.dfs(root)
        if status == 0:
            self.result += 1
        return self.result

    def dfs(self, root: TreeNode | None) -> int:
        if root is None:
            return 2
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == 2 and right == 2:
            return 0
        if left == 0 or right == 0:
            self.result += 1
            return 1
        if left == 1 or right == 1:
            return 2
        return -1
