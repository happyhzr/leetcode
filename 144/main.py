class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, current: TreeNode | None, result: list[int]) -> None:
        if current is None:
            return
        result.append(current.val)
        self.helper(current.left, result)
        self.helper(current.right, result)
