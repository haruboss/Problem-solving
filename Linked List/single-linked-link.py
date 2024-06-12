class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.no_of_nodes = 0
    
    def insert_start(self, data):
        new_node = Node(data)
        self.no_of_nodes += 1

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        self.no_of_nodes += 1

        if self.head:
            actual_node = self.head
            while actual_node.next:
                actual_node = actual_node.next
            actual_node.next = new_node
        else:
            self.head = new_node

    def size_of_linked_list(self):
        return self.no_of_nodes
    
    def middle_of_linked_list(self):
        actual_node = fast_node = self.head
        if self.head:
            while fast_node and fast_node.next:
                actual_node = actual_node.next
                fast_node = fast_node.next.next
            print(actual_node.data)
        else:
            return None

    def traverse_linked_list(self, ll=None):
        actual_node = ll or self.head 
        if(self.head):
            while actual_node:
                print(actual_node.data)
                actual_node = actual_node.next
        else:
            return None

    def traverse_backward(self):
        ll = self.reverse_linked_list()
        self.traverse_linked_list(ll)

    def reverse_linked_list(self):
        if self.head:
            actual_node = self.head
            previous_node = None
            while actual_node:
                next_node = actual_node.next
                actual_node.next = previous_node
                previous_node = actual_node
                actual_node = next_node
            self.head = previous_node

    def remove_first_node(self):
        if self.head is None:
            return None
        removing_node = self.head
        self.head = self.head.next
        return removing_node.data

    def remove_last_node(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        prev = self.head
        actual_nodes = self.head
        while actual_nodes and actual_nodes.next:
            prev = actual_nodes
            actual_nodes = actual_nodes.next
        prev.next = None

    def remove_kth_node(self, k):
        if self.head is None:
            return None
        
        if self.head.data == k:
            self.head = self.head.next
            return
            
        prev = actual_node = self.head 
        while actual_node:
            if (actual_node.data == k):
                prev.next = actual_node.next
            prev = actual_node
            actual_node = actual_node.next



       
list = SingleLinkedList()
list.insert_end(5)
list.insert_end(4)
list.insert_end(3)
list.insert_end(2)
list.insert_end(1)

list.traverse_linked_list()
# list.traverse_linked_list()
# list.reverse_linked_list()
# list.traverse_linked_list()
# print("linked list no of element: ", list.size_of_linked_list())
# list.middle_of_linked_list()
print("removing first node ",list.remove_kth_node(4)) 
list.traverse_linked_list()