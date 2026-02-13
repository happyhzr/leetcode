from collections import deque


class MyStack:
    q: deque[int]

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.helper()

    def top(self) -> int:
        item = self.helper()
        self.q.append(item)
        return item

    def empty(self) -> bool:
        return len(self.q) == 0

    def helper(self) -> int:
        l = len(self.q) - 1
        while l > 0:
            item = self.q.popleft()
            self.q.append(item)
            l -= 1
        item = self.q.popleft()
        return item
