def palindrome(A):
	B = list(A)
	A.reverse()
	if A==B:
		return True
	else:
		return False


A = [1,2,3,4,5,4,3,2]
print palindrome(A)
