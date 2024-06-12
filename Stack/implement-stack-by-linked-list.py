class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackWithLinkedList:
    
    def __init__(self):
        self.stack = None
        self.size_of_stack = 0
    
    def push(self, data):
        new_node = Node(data)
        self.size_of_stack += 1
        new_node.next = self.stack # moving stack one position ahead from new node
        self.stack = new_node # inserting new node at the beginning


    def pop(self):
        if(self.stack):
            self.size_of_stack -= 1
            t = self.stack
            self.stack = self.stack.next
            return t.data

    def peak(self):
        if self.stack:
            return self.stack.data
        return None
    
    def stack_size(self):
        return self.size_of_stack
    

    # def traverse(self):
    #     actual_node = self.stack
    #     while actual_node:
    #         print(actual_node.data)
    #         actual_node =actual_node.next

ll_list = StackWithLinkedList()
ll_list.push(3)
ll_list.push(4)
ll_list.push(1)
ll_list.push(2)
ll_list.traverse()
popped = "popped element: "

print("peak: ", ll_list.peak())
print(popped, ll_list.pop())
print("peak: ", ll_list.peak())


    
