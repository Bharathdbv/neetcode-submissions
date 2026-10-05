class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recently_used = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recently_used.remove(key)
            self.recently_used.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            # update existing
            self.recently_used.remove(key)

        elif len(self.cache) == self.capacity:
            # remove LRU
            lru = self.recently_used.pop(0)
            del self.cache[lru]

        self.cache[key] = value
        self.recently_used.append(key)