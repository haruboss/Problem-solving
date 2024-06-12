class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.head  = None
        self.last  = None

    # inserting at the end 
    def enqueue(self, data):
        new_item = Node(data)
        if self.last:
            self.last.next = new_item
            self.last = new_item
        else:
            self.head = new_item
            self.last = new_item
 
    # removing from the start 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.item
            self.head = self.head.next
            return to_return


    def isEmpty(self):
        return self.head == None


    def peak(self):
        return self.head.item


    # def traverse(self):
    #     actual_item = self.head

    #     while actual_item:
    #         print(actual_item.item)
    #         actual_item = actual_item.next

queue1 = Queue()
print('queue empty: ', queue1.isEmpty())

queue1.enqueue(0)
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
# queue1.traverse()

# print(queue1.peak()) #3
print('queue empty: ', queue1.isEmpty())
# queue1.dequeue()
# queue1.dequeue()

# print(queue1.peak()) #2