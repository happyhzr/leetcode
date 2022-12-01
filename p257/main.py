from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        paths = []
        self.dfs(root, path, paths)
        results = []
        for path in paths:
            path = [str(v) for v in path]
            results.append('->'.join(path))
        return results

    def dfs(self, node: Optional[TreeNode], path: List[int], paths: List[List[int]]):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(path)
            return
        self.dfs(node.left, path.copy(), paths)
        self.dfs(node.right, path.copy(), paths)
