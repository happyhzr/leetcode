class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        if len(nums) == 0:
            return None
        max_value = 0
        max_index = 0
        for i, v in enumerate(nums):
            if v > max_value:
                max_value = v
                max_index = i
        root = TreeNode(max_value)
        left = nums[:max_index]
        right = nums[max_index + 1 :]
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
