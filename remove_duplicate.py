old_array = [1,2,2,3,4,2,3,5]
new_array = ['\n'] * len(old_array)

new_array[0] = old_array[0] 
print new_array

for i in range(len(old_array)):
	print i
	j = 0
	while(new_array[j] != '\n'):
		print 'j ', j
		if new_array[j] == old_array[i]:
			break
		j = j + 1

	if new_array[j] == '\n':
		new_array[j] = old_array[i]

print new_array

