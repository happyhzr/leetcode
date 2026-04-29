class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums: list[int], left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        middle = (left + right) // 2
        node = TreeNode(nums[middle])
        node.left = self.dfs(nums, left, middle - 1)
        node.right = self.dfs(nums, middle + 1, right)
        return node
