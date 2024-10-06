import random

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val not in self.map:
            res = True
            self.map[val] = len(self.list)
            self.list.append(val)
        else:
            res = False
        return res
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            res = False
        else:
            res = True
            idx = self.map[val]
            last = self.list[-1]
            self.list[idx] = last
            self.map[last] = idx
            self.list.pop()
            del self.map[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()