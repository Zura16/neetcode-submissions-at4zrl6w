class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.tail = None

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
        node.next = next
        node.prev = prev

    def appendleft(self, value: int) -> None:
        node, next, prev = Node(value), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next 
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev
        return node.val
