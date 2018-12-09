#Longest Integer Subarray

a = [0,1,2,3,4,9,8,7,6,5] #north
b = [4,5,6,7,8,9,0,1,2,3] #south

d = {}
for i in range(len(a)):
	d.update({a[i]:b[i]})

print d.keys()
v = d.values()
print v

A=v

l = len(A)

lis = [1] * l
lis_arr = []
for i in range(1, l):
	for j in range(i):
		if A[i] > A[j]:
#			lis[i] = max(lis[j]+1, lis[i])
			if lis[j] + 1 > lis[i]:
				lis[i] = lis[j] + 1

m = max(lis)

s = 6
for i in range(l-1, -1, -1):
	if lis[i] == s:
		lis_arr.insert(0, A[i])
		s -= 1

print A
print lis
print m
print lis_arr

	
