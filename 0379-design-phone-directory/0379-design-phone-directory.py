class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.dir = set(range(maxNumbers))
        
    def get(self) -> int:
        number = -1
        if self.dir:
            number = self.dir.pop()
        return number

    def check(self, number: int) -> bool:
        return number in self.dir

    def release(self, number: int) -> None:
        self.dir.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)