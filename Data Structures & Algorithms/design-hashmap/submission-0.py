class MyHashMap:

    def __init__(self):
        self.res = {}

    def put(self, key: int, value: int) -> None:
        self.res[key] = value

    def get(self, key: int) -> int:
        if key in self.res:
            return self.res[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.res:
            self.res.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)