class RecentCounter:

    def __init__(self):
        self.range = []
        self.requests = []
        self.res = 0  

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.range = [t-3000, t]
        
        i = 0
        while(i<len(self.requests)):
            if self.requests[i] not in range(self.range[0], self.range[1] + 1):
                self.requests.pop(0)
                i -= 1
            i+=1

        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)