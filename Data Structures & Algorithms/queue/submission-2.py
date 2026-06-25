class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        curr = Node(value)
        prev = self.tail.prev
        next = self.tail
        prev.next = curr
        next.prev = curr
        curr.prev = prev
        curr.next = next

    def appendleft(self, value: int) -> None:
        curr = Node(value)
        prev = self.head
        next = self.head.next
        prev.next = curr
        next.prev = curr
        curr.prev = prev
        curr.next = next

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.tail.prev
        value = curr.val
        prev = curr.prev
        next = self.tail
        prev.next = next
        next.prev = prev
        return value

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.head.next
        value = curr.val
        prev = self.head
        next = curr.next
        prev.next = next
        next.prev = prev
        return value

