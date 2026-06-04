class Queue:
    def __init__(self):
        self.items = []
    
    def append_front(self, value):
        self.items.append(value)
        
    def remove_front(self):
        return self.items.pop(0)
        
    def display(self):
        for item in self.items:
            print(item)
            
q1 = Queue()
q1.append_front(10)
q1.append_front(20)

q1.display()

print(q1.remove_front())
q1.display()
