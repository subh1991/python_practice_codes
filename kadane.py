a = [-1, -1, 1, 1,1, -1, 1, -1]

temp1 = temp2 = a[0]
s = e = 0

for i in range(len(a)):
#	temp1 = max(a[i], temp1+a[i])
#	temp2 = max(temp1, temp2)

	if a[i] >= temp1 + a[i]:
		temp1 = a[i]
		s = i
	else:
		temp1 = temp1 + a[i]

	if temp1 > temp2:
		temp2 = temp1
		e = i
	else:
		pass

print temp2, s, e
