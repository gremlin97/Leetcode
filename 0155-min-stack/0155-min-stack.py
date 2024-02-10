class MinStack:

    def __init__(self):
        self.stack = []
        self.t = 0
        self.l = 0
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.l = len(self.stack)
        self.t = self.stack[self.l - 1]
        
        if val<self.min:
            self.min = val
        
    def pop(self) -> None:
        self.stack.pop()
        self.l -= 1
        if self.l == 0:
            self.t = 0
            self.min = float('inf')
        else:
            self.t = self.stack[self.l - 1]
            self.min = sorted(self.stack)[0]
        
    def top(self) -> int:
        return self.t
        
    def getMin(self) -> int:
        return self.min
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()