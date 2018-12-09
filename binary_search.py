def binary_search(arr, a):
	if len(arr) == 1 and arr[0] != a:
		return False
		
	if a == arr[int(len(arr)/2)]:
		return True

	elif a > arr[int(len(arr)/2)]:
		return binary_search(arr[int(len(arr)/2 ) : int(len(arr))] ,a)
	elif a < arr[len(arr)/2]:
		return binary_search(arr[0 : int(len(arr)/2) ] ,a)



arr = [1,2,3,4,5]

print binary_search(arr, -6)
