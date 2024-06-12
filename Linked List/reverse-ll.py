class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def traverse(self):
        actual_node = self.head 
        if(self.head):
            while actual_node:
                print(actual_node.data)
                actual_node = actual_node.next
        else:
            return None
    
    def reverseList(self):
        if not self.head or not self.head.next:
            return self.head
        prev = None
        while self.head:
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev
    
    

linkedList = LinkedList()	

linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(2)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(3)

linkedList.traverse()
print("below reveres list: ")
linkedList.reverseList()
linkedList.traverse()
