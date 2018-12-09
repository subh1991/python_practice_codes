e = 4
f = 8

mat = [ [100] * (e+1) for i in range(f+1)]

for i in range(e+1):
	mat[0][i] = 0
	mat[1][i] = 1

for i in range(1, f+1):
	mat[i][0] = 0
	mat[i][1] = i


for i in range(2, e+1):
	for j in range(2, f+1):
		temp = []
		for x in range(1, j):
			temp.append(1 + max(mat[x-1][i-1], mat[j-x][i]))
		mat[j][i] = min(temp)
			
for i in range(f+1):
	print mat[i][:]
