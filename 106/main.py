class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if len(inorder) == 0:
            return None
        root_value = postorder[-1]
        root = TreeNode(root_value)
        index = 0
        for i, v in enumerate(inorder):
            if v == root_value:
                index = i
                break
        inorder_left = inorder[:index]
        inorder_right = inorder[index + 1 :]
        postorder_left = postorder[: len(inorder_left)]
        postorder_right = postorder[len(inorder_left) : -1]
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
