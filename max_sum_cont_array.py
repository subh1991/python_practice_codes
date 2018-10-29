class Array:
	def __init__(self, arr):
		self.arr = arr
	def max_sum_cont_arr(self):
		end_index = 0
		max_so_far = max_ending_here = self.arr[0]
		for i in range(1, len(self.arr)):
			max_ending_here += self.arr[i]
			if max_ending_here >= max_so_far:
				max_so_far = max_ending_here
				end_index = i
#			max_so_far = max(max_so_far, max_ending_here)
		sub_set = []
		sum_val = self.arr[end_index]
		while sum_val != max_so_far and j != -1:
			sub_set.insert(0, self.arr[i])
		return max_so_far, sub_set

def main():
	print "Hello World"
	a = Array([1,-2,3,4])
	max_sum, sub_set = a.max_sum_cont_arr()
	print max_sum
	print sub_set

if __name__ == "__main__":
	main()
