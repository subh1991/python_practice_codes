M = [[0, 0, 0], 
    [0, 1, 0], 
    [0, 0, 0]]

r = len(M)
c = len(M[0])

aux = [[0] * c for i in range(r)]

for i in range(r):
	aux[i][0] = 1
for i in range(c):
	aux[0][i] = 1

for i in range(1, r):
	for j in range(1, c):
		if M[i][j] != 1:
			aux[i][j] = aux[i-1][j] + aux[i][j-1]

print aux
