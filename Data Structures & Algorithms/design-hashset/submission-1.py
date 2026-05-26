class MyHashSet:

    def __init__(self):
        self.res = {}

    def add(self, key: int) -> None:
        self.res[key] = {}

    def remove(self, key: int) -> None:
        if key in self.res:
            self.res.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.res:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)