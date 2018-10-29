class Data:
	def __init__(self, name = "", roll = 0, lab = ""):
		self.name = name
		self.roll = roll
		self.lab = lab

class Node:
	def __init__(self, data = None, next_ptr = None, prev_ptr = None ):
		self.next_ptr = next_ptr
		self.prev_ptr = prev_ptr
		self.data = data

class DoublyLinkedList:
	def __init__(self, head = None, length = 0):
		self.head = head
		self.length = length

	def print_linked_list(self):
		temp_ptr = self.head
		while temp_ptr != None:
			print "Name:", temp_ptr.data.name, " Roll:", temp_ptr.data.roll, " Lab:", temp_ptr.data.lab
			temp_ptr = temp_ptr.next_ptr

	def add_node_at_beginning(self, data):
		node = Node(data)
		if self.length == 0:
			self.head = node
		else:
			node.next_ptr = self.head
			self.head.prev_ptr = node
			self.head = node
		self.length += 1

	def add_node_at_end(self, data):
		node = Node(data)
		temp_ptr = self.head
		while temp_ptr.next_ptr != None:
			temp_ptr = temp_ptr.next_ptr
		temp_ptr.next_ptr = node
		node.prev_ptr = temp_ptr
		self.length += 1

	def add_node_at_nth_position(self, n, data):
		if self.length == 0:
			print "No element in the list. Adding data as first node."
			self.add_node_at_beginning(data)
			return
		if self.length == 1:
			self.add_node_at_beginning(data)
			return
		node = Node(data)
		temp_ptr = self.head
		for i in range(n-2):
			temp_ptr = temp_ptr.next_ptr
		node.prev_ptr = temp_ptr
		node.next_ptr = temp_ptr.next_ptr
		temp_ptr.next_ptr.prev_ptr = node
		temp_ptr.next_ptr = node
		self.length += 1
			
	def remove_nth_node(self, n):
		if n<1 or n>self.length:
			print "Please enter a node number between 1 and ", self.length
			return
		if n ==1:
			self.head = self.head.next_ptr
			self.head.prev_ptr.prev_ptr = None
			self.head.prev_ptr.next_ptr = None
			self.head.prev_ptr = None
			self.length -= 1
			return
		temp_ptr = self.head
		for i in range(n-1):
			temp_ptr = temp_ptr.next_ptr
		temp_ptr.prev_ptr.next_ptr = temp_ptr.next_ptr
		temp_ptr.next_ptr.prev_ptr = temp_ptr.prev_ptr
		temp_ptr.prev_ptr = None
		temp_ptr.next_ptr = None
		self.length -= 1
		
	def print_list_in_reverse_order(self):
		temp_ptr = self.head
		for i in range(self.length-1):
			temp_ptr = temp_ptr.next_ptr
		while temp_ptr != None:
			print "Name:", temp_ptr.data.name, " Roll:", temp_ptr.data.roll, " Lab:", temp_ptr.data.lab
			temp_ptr = temp_ptr.prev_ptr


def main():
	print "Hello world"
	dlinkedlist = DoublyLinkedList()
	data = Data("a", 12, "aarg1")
	dlinkedlist.add_node_at_beginning(data)
	data = Data("b", 13, "aarg2")
	dlinkedlist.add_node_at_beginning(data)
	data = Data("c", 14, "aarg3")
	dlinkedlist.add_node_at_beginning(data)
	data = Data("d", 15, "aarg4")
	dlinkedlist.add_node_at_beginning(data)
	data = Data("e", 16, "aarg5")
	dlinkedlist.add_node_at_end(data)
	data = Data("f", 17, "aarg6")
	dlinkedlist.add_node_at_end(data)
	data = Data("x", 172, "aarg100")
	dlinkedlist.add_node_at_nth_position(3, data)
	data = Data("y", 171, "aarg101")
	dlinkedlist.add_node_at_nth_position(5, data)

	dlinkedlist.print_linked_list()
	print "Length of list:", dlinkedlist.length

	dlinkedlist.remove_nth_node(1)
	dlinkedlist.print_linked_list()
	print "Length of list:", dlinkedlist.length

	dlinkedlist.remove_nth_node(4)
	dlinkedlist.print_linked_list()
	print "Length of list:", dlinkedlist.length

	dlinkedlist.print_list_in_reverse_order()
	print "Length of list:", dlinkedlist.length

if __name__ == '__main__':
	main()














