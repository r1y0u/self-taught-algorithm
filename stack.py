
class Mystack:
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) -1
        return self.items[last]
    
    def size(self):
        return len(self.items)   

stack = Mystack()

print(stack.is_empty())
# True

stack.push(3)
item = stack.pop()
print(item)
print(stack.is_empty())
# 3 , True

for i in range(1,8):
    stack.push(i)
    
print(stack.peek())  
print(stack.size())
# 7, 7
