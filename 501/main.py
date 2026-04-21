class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre: TreeNode | None
    count: int
    max_count: int
    result: list[int]

    def __int__(self):
        self.pre = None
        self.count = 0
        self.max_count = 0
        self.result = []

    def findMode(self, root: TreeNode | None) -> list[int]:
        self.pre = None
        self.count = 0
        self.max_count = 0
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, cur: TreeNode | None) -> None:
        if not cur:
            return
        self.dfs(cur.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = cur
        if self.count == self.max_count:
            self.result.append(cur.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.result.clear()
            self.result.append(cur.val)
        self.dfs(cur.right)
        return None
