class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node, next, prev = Node(value), self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.prev = prev 
        node.next = next

    def appendleft(self, value: int) -> None:
        node, next, prev = Node(value), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.prev = prev 
        node.next = next

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.tail.prev
        next = curr.next
        prev = curr.prev
        prev.next = next
        next.prev = prev
        return curr.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.head.next
        next = curr.next
        prev = curr.prev
        prev.next = next
        next.prev = prev
        return curr.val
