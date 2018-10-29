class Stack:
	def __init__(self, size = 5):
		self.s = []
		self.minElm = None
		self.size = size
	
	def print_stack(self):
		print self.s, "min element: ",self.minElm

	def push(self, data):
		if len(self.s) == self.size:
			print "Stack Over flow."
			return
		if len(self.s) == 0:
			self.s.append(data)
			self.minElm = data
			return
		if data >= self.minElm:
			self.s.append(data)
		else:
			self.s.append(2*data - self.minElm)
			self.minElm = data

	def pop(self):
		if (len(self.s) == 0):
			print "stack is empt."
			return
		if self.s[-1] < self.minElm:
			temp = self.minElm
			self.minElm = 2 * self.minElm - self.s.pop()
			return temp
		else:
			return self.s.pop()


def main():
	print "Hello World."
	stack = Stack()
	stack.push(7)
	stack.push(5)
	stack.push(3)
	stack.push(6)
	print stack.pop()	
	print stack.pop()	
	stack.push(2)
	stack.push(8)
	stack.push(1)
	stack.push(1)
	stack.push(1)
	stack.print_stack()
	print stack.pop()	
	print stack.pop()	
	print stack.pop()	
	print stack.pop()	
	print stack.pop()	

if __name__ == "__main__":
	main()











