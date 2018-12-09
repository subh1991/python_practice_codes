def merge_sort(arr):
	if len(arr) == 1:
		return arr
	l = arr[0:len(arr)/2]
	r = arr[len(arr)/2 : len(arr)]

	l = merge_sort(l)
	r = merge_sort(r)

	temp_arr = []

	i = j = 0
	while True:
		if l[i] <= r[j]:
			temp_arr.append(l[i])
			i += 1
		elif r[j] <= l[i]:
			temp_arr.append(r[j])
			j += 1

		if i == len(l) and j == len(r):
			break
		elif i == len(l):
			temp_arr.append(r[j])
			break
		elif j == len(r):
			temp_arr.append(l[i])
			break
	return temp_arr


def main():
	print "Hello world"
	a = [4,6,3,8,2,5,7,1]
	print merge_sort(a)


if __name__ == '__main__':
	main()	
