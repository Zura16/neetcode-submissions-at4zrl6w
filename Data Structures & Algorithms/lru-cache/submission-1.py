class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        next, prev = self.right, self.right.prev
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])
        if len(self.hm) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hm[lru.key]