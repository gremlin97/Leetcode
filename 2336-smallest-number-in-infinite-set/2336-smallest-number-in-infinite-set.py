import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1,10001))
        self.heap_set = set(self.heap)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        small =  heapq.heappop(self.heap)
        self.heap_set.remove(small)
        return small
        
    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
            self.heap_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)