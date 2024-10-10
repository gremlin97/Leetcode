class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None
    def __str__(self):
        return "Key "+ str(self.key)+ " val "+ str(self.value)
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left 
    # def printt(self):
    #     for key in self.cache:
    #         print(key, self.cache[key])
    #     print("done")
        
    def remove(self, key):
        rem = self.release(self.cache[key])
        del rem
        del self.cache[key]
    
    def insert(self, node):
        p, n = self.right.prev, self.right
        # print(p.value)
        node.next = n
        node.prev = p
        p.next = node
        n.prev =  node
    
    def release(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None
        return node
            
    def get(self, key: int) -> int:
        # self.printt()
        if key in self.cache:
            self.release(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        # print('Val',self.cache[key].value)
        return -1

    def put(self, key: int, value: int) -> None:
        # print("put", key)
        
        if key in self.cache:
            self.remove(key)
            # node = Node(key, value)
            # self.insert(node)
            # self.cache[key] = node
        new = Node(key, value)
        self.cache[key] = new
        self.insert(new)
        if len(self.cache) > self.cap:
            # print(self.left.next.key, self.cache)
            self.remove(self.left.next.key)
        # self.printt()
#         else:
#             print('Here')
#             if self.cap == len(self.cache.items()):
#                 lru = self.left.next
#                 self.remove(lru)
            
#             node = Node(key, value)
#             self.insert(node)
#             self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)