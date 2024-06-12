class Stack:
    def __init__(self):
        self.stack_memory = []
        self.max = 0
    
    def add(self, data):
        self.stack_memory.append(data)

        if(self.max < data):
            self.max = data

        return data


    def get_max(self):
       return self.max


stack_lifo = Stack()

stack_lifo.add(1)
stack_lifo.add(2)
stack_lifo.add(32)
stack_lifo.add(2)
stack_lifo.add(2)
stack_lifo.add(6)
print(stack_lifo.get_max())