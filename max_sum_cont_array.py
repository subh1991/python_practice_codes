class Array:
	def __init__(self, arr):
		self.arr = arr
	def max_sum_cont_arr(self):
		temp_sum = self.arr[0]
		max_sum = self.arr[0]
		for i in range(1, len(self.arr)):
			temp_sum = max(self.arr[i], temp_sum+self.arr[i])
			max_sum = max(temp_sum, max_sum)

		return max_sum

	def max_sum_cont_arr_with_subarr(self):
		temp_sum = self.arr[0]
		max_sum = self.arr[0]
		l = r = 0
		for i in range(1, len(self.arr)):
			if self.arr[i] > temp_sum + self.arr[i]:
				l = i
				temp_sum = self.arr[i]
			else:
				temp_sum = temp_sum + self.arr[i]
			if temp_sum > max_sum:
				max_sum = temp_sum
				r = i
		return max_sum, self.arr[l:r+1]

	def min_sum_cont_arr(self):
		temp_sum = min_sum = self.arr[0]
		l = r = 0
		for i in range(1, len(self.arr)):
#			temp_sum = min(self.arr[i], temp_sum+self.arr[i])
#			min_sum = min(temp_sum, min_sum)
			if self.arr[i] < temp_sum + self.arr[i]:
				temp_sum = self.arr[i]
				l = i
			else:
				temp_sum = temp_sum + self.arr[i]
			if temp_sum < min_sum:
				min_sum = temp_sum
				r = i
		return min_sum, self.arr[l:r+1]

def main():
	print "Hello World"
	a = Array([1,-2,3,4, -2, 3, 1, -1, -4])
	max_sum, sub_arr = a.max_sum_cont_arr_with_subarr()
	print a.arr
	print max_sum, sub_arr
	min_sum, min_sub_arr = a.min_sum_cont_arr()
	print a.arr
	print min_sum, min_sub_arr

if __name__ == "__main__":
	main()











