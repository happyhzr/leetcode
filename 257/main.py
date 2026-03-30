class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths = []
        self.helper(root, [], paths)
        results = []
        for path in paths:
            results.append("->".join(path))
        return results

    def helper(
        self, node: TreeNode | None, path: list[str], paths: list[list[str]]
    ) -> None:
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            paths.append(path)
            return
        self.helper(node.left, path.copy(), paths)
        self.helper(node.right, path.copy(), paths)
