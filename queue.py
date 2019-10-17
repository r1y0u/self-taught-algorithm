class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

myqueue = Queue()
print(myqueue.is_empty())
#True

for i in range(3):
    myqueue.enqueue(i)
    print(myqueue)
#<__main__.Queue instance at 0x1033c6ea8>
#<__main__.Queue instance at 0x1033c6ea8>
#<__main__.Queue instance at 0x1033c6ea8>

print(myqueue.size())
# 3

print("\n")

while myqueue.size():
    print(myqueue.dequeue())
# 0
# 1
# 2

print("\n")
print(myqueue.size())
# 0