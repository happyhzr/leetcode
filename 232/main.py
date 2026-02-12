class MyQueue:
    in_stack: list[int]
    out_stack: list[int]

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        result = self.peek()
        self.out_stack.pop()
        return result

    def peek(self) -> int:
        self.helper()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def helper(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                item = self.in_stack.pop()
                self.out_stack.append(item)
