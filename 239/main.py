from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = Queue()
        result = []
        for i in range(k):
            q.push(nums[i])
        result.append(q.front())
        for i in range(k, len(nums)):
            q.pop(nums[i - k])
            q.push(nums[i])
            result.append(q.front())
        return result


class Queue:
    queue: deque[int]

    def __init__(self):
        self.queue = deque()

    def pop(self, value: int) -> None:
        if len(self.queue) != 0 and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value: int) -> None:
        while len(self.queue) != 0 and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]
