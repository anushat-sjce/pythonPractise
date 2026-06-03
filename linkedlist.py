class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_last(self, value):
        new_node = Node(value)
        current = self.head
        
        if not self.head:
            self.head = new_node
            return
        current = self.head
        
        while current.next :
            current = current.next
        
        current.next = new_node
        
    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        
    def append_begin(self, value):
        new_node = Node(value)
        
        current = self.head
        if not current:
            self.head = new_node
            return
        current = self.head
        new_node.next = current
        self.head = new_node
    
    def delete_end(self):
        current = self.head
        while(current.next):
            prev = current
            current = current.next
        prev.next = None
        
    def delete_front(self):
        current = self.head
        current = current.next
        self.head = self.head.next

ll = LinkedList()
ll.append_last(10)
ll.append_last(20)
#ll.display()
#print("hello")
ll.append_begin(30)
ll.append_begin(40)
#ll.display()
print("hello")
#ll.delete_end()
ll.display()
print("hello")
ll.delete_front()
ll.display()
