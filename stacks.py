class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
        
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
        
s2 = Stack()
s2.push(40)
s2.push(30)
s2.push(20)
