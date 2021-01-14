class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.order = deque()
        self.timestamp = 0
        self.last_checked = 0
        

    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.cache[key][1] = self.timestamp
        self.timestamp += 1
        self.order.append(key)
        
        return self.cache[key][0]
        

    def put(self, key, value):
        if key not in self.cache and len(self.cache) == self.cap:
            lru = self.order.popleft()
            while lru not in self.cache or self.cache[lru][1] != self.last_checked:
                self.last_checked += 1
                lru = self.order.popleft()
            del self.cache[lru]
            self.last_checked += 1
            
        self.cache[key] = [value, self.timestamp]
        self.timestamp += 1
        self.order.append(key)