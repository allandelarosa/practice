class LRUCache(object):
    class Node(object):
        def __init__(self, val=0, key=0, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next
        
        
    def _move_to_end(self, key):
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        
        self.cache[key].prev = self.tail.prev
        self.cache[key].next = self.tail
        
        self.tail.prev.next = self.cache[key]
        self.tail.prev = self.cache[key]
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.len = 0
        self.cache = {}
        self.head = self.Node()
        self.tail = self.Node(prev=self.head)
        self.head.next = self.tail

        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self._move_to_end(key)
        
        return self.cache[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._move_to_end(key)
            self.cache[key].val = value
        else:
            self.cache[key] = self.Node(value, key, self.tail.prev, self.tail)
            self.tail.prev.next = self.cache[key]
            self.tail.prev = self.cache[key]
            self.len += 1
            
        if self.len > self.cap:
            to_remove = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.cache[to_remove.key]
            self.len -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)