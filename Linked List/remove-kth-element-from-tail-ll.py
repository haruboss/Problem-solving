class LinkedList:
    def __init__(self):
        self.head = None
        
    def remove_kth_node(self, k):
        if self.head is None:
            return None
    
        if self.head.data == k:
            self.head = self.head.next
            return None
        
        prev = actual_node = self.head 
        while actual_node:
            if (actual_node.data == k):
                prev.next = actual_node.next
            prev = actual_node
            actual_node = actual_node.next

