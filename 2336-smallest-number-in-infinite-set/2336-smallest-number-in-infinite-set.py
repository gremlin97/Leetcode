import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1,10001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            small =  heapq.heappop(self.heap)
            print(small)
            return small
        
    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)