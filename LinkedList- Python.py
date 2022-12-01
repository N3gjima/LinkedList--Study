class Node:
	def __init_(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def append(self, elem):
		if self.head:
			while(pointer.next):
				pointer = pointer.next
			pointer.next = Node(elem)
		else:
			self.head = Node(elem)
		self.size = self.size + 1

	def __len__(self):
		return self.size

	def __getitem__(self, index):
		pointer = self.head
		for i in range(index):
			if pointer:
				pointer = pointer.next 
			else:
				raise IndexError("List index error out of range")	
		if pointer: 
			return pointer.data
		raise IndexError("list index out of range")

	def __setitem__(self, index, elem):
		pointer = self.head
		for i in range(index):
			if pointer:
				pointer = pointer.next
			else:
				raise IndexError("List index error out of range")
		if pointer:
			pointer.data = elem
		else:
			raise IndexError("List index error out of range")
	def index (self,elem):
		pointer = self.head
		i = 0
		while(pointer):
			if pointer.data == elem:
				return
			pointer = pointer.next
			i = i + 1 
		raise ValueError ("{} is not in list".format(elem))
