from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        q = deque[TreeNode]()
        if root:
            q.append(root)
        while q:
            size = len(q)
            vector = []
            while size > 0:
                node = q.popleft()
                vector.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
            result.append(vector)
        return result
