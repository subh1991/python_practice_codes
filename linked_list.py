class Node:
	def __init__(self, data = 0, ptr = None):
		self.data = data
		self.ptr = ptr


class LinkedList:
	def __init__(self, root = None, length = 0):
		self.root = root
		self.length = length

	def print_linked_list(self):
		list_to_print = []
		travese_ptr = self.root
		while True:
			list_to_print.append(travese_ptr.data)
			if travese_ptr.ptr == None:
				break
			travese_ptr = travese_ptr.ptr
		print list_to_print

	def add_node_at_beginning(self, data):
		node = Node(data)
		node.ptr = self.root
		self.root = node
		self.length += 1 
		return True, self.length

	def add_node_at_end(self, data):
		if self.root == None:
			retval = self.add_node_at_beginning(data)
			return retval

		travese_ptr = self.root
		while True:
			travese_ptr = travese_ptr.ptr
			if travese_ptr.ptr == None:
				break
		node = Node(data)
		travese_ptr.ptr = node
		self.length += 1
		return True, self.length

	def add_node_after_nth_node(self, n, data):
		if self.root == None:
			print "No element in Linked List. Adding data as first node."
			retval = self.add_node_at_beginning(data)
			return retval
		if n<1 or n >self.length:
			print "Please provide value between 1 and ", self.length
			return False, self.length
		node = Node(data)
		travese_ptr = self.root
		for i in range(1, n):
			travese_ptr = travese_ptr.ptr
		node.ptr = travese_ptr.ptr
		travese_ptr.ptr = node
		self.length += 1
		return True, self.length

	
	def remove_nth_node(self, n):
		if n<1 or n>self.length or self.root == None:
			if self.root != None:
				print "Please provide value between 1 and ", self.length
			else:
				print "No element in Linked List"
			return False, self.length
		if n == 1:
			travese_ptr = self.root
			self.root = travese_ptr.ptr
			self.length -= 1
			return True, self.length
		
		travese_ptr = self.root
		for i in range(1, n-1):
			travese_ptr = travese_ptr.ptr
		temp_ptr = travese_ptr.ptr
		temp_ptr = temp_ptr.ptr
		travese_ptr.ptr = temp_ptr
		self.length -= 1
		return True, self.length
	def reverse_linked_list(self):
		if self.length == 0 or self.length==1:
			if self.length == 0:
				print "No element in the list."
			if self.length == 1:
				print "Only one element in the list."
			return True, self.length
		for i in range(self.length-1):
			if i == 0:
				prev_node = self.root
				current_node = prev_node.ptr
				next_node = current_node.ptr
				prev_node.ptr = None
				current_node.ptr = prev_node
				prev_node = current_node
				current_node = next_node
				self.root = current_node
			else:
				next_node = current_node.ptr
				current_node.ptr = prev_node
				prev_node = current_node
				current_node = next_node
				self.root = prev_node
			
			
			
			
				


def main():
	print "Hello World..."

	linkedList = LinkedList()

	retval = linkedList.add_node_at_end(80)
	print retval
	retval = linkedList.add_node_at_beginning(10)
	print retval
	retval = linkedList.add_node_at_beginning(20)
	print retval
	retval = linkedList.add_node_at_beginning(30)
	print retval

	retval = linkedList.add_node_at_end(60)
	print retval
	retval = linkedList.add_node_at_end(70)
	print retval
	retval = linkedList.add_node_after_nth_node(2, 100)

	linkedList.print_linked_list()
	print "Length of the linked list: ", linkedList.length
	linkedList.reverse_linked_list()
	print "Printing reverse Linked List: "
	linkedList.print_linked_list()


	linkedList.remove_nth_node(9)
	linkedList.print_linked_list()
	print "Length of the linked list: ", linkedList.length

	linkedList2 = LinkedList()
	retval = linkedList2.add_node_at_beginning(12)
	retval = linkedList2.remove_nth_node(1)
	retval = linkedList2.remove_nth_node(5)
	linkedList2.print_linked_list
	print "Length of the linked list2: ", linkedList2.length
	linkedList2.add_node_after_nth_node(2, 21)
	linkedList2.print_linked_list()	

def main2():
	linkedList = LinkedList()
	retval = linkedList.add_node_at_end(1)
	retval = linkedList.add_node_at_end(2)
	retval = linkedList.add_node_at_end(3)
	retval = linkedList.add_node_at_end(4)
	retval = linkedList.add_node_at_end(5)
	retval = linkedList.add_node_at_end(6)
	retval = linkedList.add_node_at_end(7)
	linkedList.print_linked_list()


if __name__ == '__main__':
	main2()
















