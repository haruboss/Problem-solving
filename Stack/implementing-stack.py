class Stack: #LIFO

    def __init__(self):
        self.stack = []


    def push(self, data):
        # "Pushing new item into the stack.. "
        return self.stack.append(data)


    def pop(self):
        if self.size_of_stack() < 1:
            return None
        pop_item = self.stack[-1]
        # "Popped or removed the item from the stack."
        del self.stack[-1]
        return pop_item


    def size_of_stack(self):
        return len(self.stack)


    def peak(self):
        if self.size_of_stack():
            # "Peak/top item into the stack.. "
            return self.stack[-1]
        return None


stack_lifo = Stack()

stack_lifo.push(1)
stack_lifo.push(2)
stack_lifo.push(3)

print(stack_lifo.peak())
print("Stack size: ", stack_lifo.size_of_stack())

print(stack_lifo.pop())

print(stack_lifo.peak())
print("Stack size: ", stack_lifo.size_of_stack())