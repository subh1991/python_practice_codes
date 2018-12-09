M = [[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]] 

r = len(M)
c = len(M[0])

aux = [[0] * c for i in range(r)]

for i in range(r):
	aux[i][0] = M[i][0]
for i in range(c):
	aux[0][i] = M[0][i]

for i in range(1, r):
	for j in range(1, c):
		if M[i][j] != 0:
			aux[i][j] = min(aux[i-1][j], aux[i][j-1], aux[i-1][j-1]) + 1


m =  max(max(x) for x in aux)
print m
for i in range(r):
	if m in aux[i]:
		p_x = i
		p_y = aux[i].index(m)
		break

print p_x, p_y
