class MyCalendar:

    def __init__(self):
        self.intervals = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.intervals:
            '''
            |s     e|  |start   end|
            |s       |start    e|   end|
            
            '''
            
            if start<e and end>s:
                return False
        self.intervals.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)