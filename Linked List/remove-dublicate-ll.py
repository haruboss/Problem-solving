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

	def removeDuplicate(self):
		if self.head:
			actual_node = self.head
			while actual_node and actual_node.next:
				print(actual_node)
				if (actual_node.data == actual_node.next.data):
					actual_node = actual_node.next.next
				else:
					actual_node = actual_node.next	


linkedList = LinkedList()	

linkedList.insert(1)
linkedList.insert(2)
linkedList.insert(2)
linkedList.insert(2)
linkedList.insert(3)
linkedList.insert(3)

linkedList.removeDuplicate()
