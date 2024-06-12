capacity = 10

class Heap:
    def __init__(self):
        # this is the actual number of item in the data structure
        self.heap_size = 0
        self.heap = [0] * capacity

    def insert(self, item):
        if self.heap_size == capacity:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap properties
        # size minus one because index start from zero
        self.fix_up(self.heap_size - 1) 


    # start with the actual node we have inserted up to root node
    # we have to compare the value weather to make swap operation or not
    # time complexity O(logN)
    def fix_up(self, index):

        parent_index = (index - 1)//2

        # we have consider all the item till we hit the root node
        # if the heap property violated we will swap the parent-child

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)


    def get_max(self):
        if len(self.heap) > 0:
            return self.heap[0]
        
        
    def poll(self):
        max_item = self.get_max()

        # swap the root node with the last item and heapify
        self.heap[0], self.heap[self.heap_size -1] = self.heap[self.heap_size -1], self.heap[0]

        # make sure heap is heapify
        self.fix_down(0)

        return max_item

    def fix_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        # in a max heap parent is always greater then its children 

        largest_index = index
        
        # looking for the largest (parent or left node)
        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            largest_index = index

        if index_right < self.heap_size and self.heap[index_right] > self.heap[index]:
            largest_index = index

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.fix_down(largest_index)



    def heap_sort(self):
        for _ in range(self.heap_size):
            max_item = self.get_max()
            print(max_item)

heap = Heap()

heap.insert(1)
heap.insert(4)
heap.insert(-1)
heap.insert(97)

heap.heap_sort()

