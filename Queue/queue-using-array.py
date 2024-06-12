class Queue: #FIFO
    def __init__(self):
        self.qu = []

    def enqueue(self, data):
        self.qu.append(data)
        return data

    def dequeue(self):
        if self.is_empty():
            return None
        
        dequeue_element = self.qu[0]
        del self.qu[0]
        return dequeue_element

    def peak(self):
        if self.is_empty():
            return None
        
        return self.qu[0]

    def is_empty(self):
        return self.qu == []

    def size_of_queue(self):
        return len(self.qu)

            
queue = Queue()


queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.dequeue()  

print("peak " ,queue.peak())


