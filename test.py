class String:
	def __init__(self, s = ""):
		self.s = s

	def print_s(self):
		print self.s

	def length_LPS(self):
		l = len(self.s)
		mat = [[0] * l for i in range(l)]
		for i in range(l):
			mat[i][i] = 1
		
		for i in range(l):
			while j < l:
				if self.s[i] == self.s[j]:
					mat[i][j] = mat[i+1][j-1] + 2
				else:
					mat[i][j] = max(mat[i][j-1], mat[i+1][j])
				j += 1
		print mat


def main():
	string = String("Hello World")
	string.print_s()
	string.length_LPS()

if __name__ == "__main__":
	main()
