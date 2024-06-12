# insert start, end - done
# remove start, end - done
# traverse start, end - done
# size of linked list - done
# middle of linked list 
# reverse of linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size_of_nodes = 0

    def insert_start(self, data):
        self.size_of_nodes += 1
        new_node = Node(data)

        if self.head:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node

    def insert_end(self, data):
        self.size_of_nodes += 1
        new_node = Node(data)

        if self.head:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def remove_start(self):
        if self.head is None:
            print("ths list has no element to delete")
            return None
        
        if self.head.next_node is None:
            print(self.head.data, "removed.")
            self.head = None
            return
        
        self.head = self.head.next_node
        self.head.prev_node = None

    def remove_end(self):
        if self.head is None:
            print("the list has no element to delete.")
            return True
        if self.head.next_node is None:
            self.head = None
            return True
        self.tail = self.tail.prev_node
        self.tail.next_node = None 

    def traverse_forward(self):
        actual_node = self.head
        if actual_node:
            while actual_node:
                print(actual_node.data)
                actual_node =  actual_node.next_node
        return "The list is empty."

    def traverse_backward(self):
        last_node = self.tail
        if last_node:
            while last_node:
                print(last_node.data)
                last_node = last_node.prev_node

    def size_of_linked_list(self):
        return self.size_of_nodes

    def middle_of_linked_list(self):
        if self.head is None:
            return "The list has no element."
        if self.head.next_node is None:
            print(self.head.data)
            return True
        
        slow = fast = self.head
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node
        print(slow.data)

    def reverse_linked_list(self):
        pass

        # Function reverse a Doubly Linked List
    
    def reverse(self):
        temp = None
        current = self.head
 
        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
 
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev


            



linked_list = DoublyLinkedList()

linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)

# linked_list.remove_end()

linked_list.middle_of_linked_list()