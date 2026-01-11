from __future__ import annotations


class MyLinkedList:
    dummy: ListNode
    size: int

    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        current = self.dummy.next
        while index > 0 and current is not None:
            current = current.next
            index -= 1
        if current is None:
            return -1
        return current.value

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        current = self.dummy
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new_node = ListNode(val)
        current = self.dummy
        while index > 0 and current is not None:
            current = current.next
            index -= 1
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        current = self.dummy
        while index > 0 and current is not None:
            current = current.next
            index -= 1
        if current is None:
            return
        if current.next is None:
            return
        current.next = current.next.next
        self.size -= 1


class ListNode:
    value: int
    next: ListNode | None

    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
