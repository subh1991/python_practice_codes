import stack

def get_val(op, val1, val2):
	switch = {
			'+': val1 + val2,
			'-': val1 - val2, 
			'*': val1 * val2, 
			'/': val1 / val2
		 }
	return switch[op]

def evaluate_postfix_in_switch(expr):
	s = stack.Stack(len(expr))
	expr = expr.split()
	ans = 0
	for i in range(len(expr)):
		if expr[i] != '+' and expr[i] != '-' and expr[i] != '*' and expr[i] != '/': 
			s.push(float(expr[i]))
		else:
			val2 = s.pop()
			val1 = s.pop()
			ans = get_val(expr[i], val1, val2)
			
			s.push(ans)	
	return ans

def evaluate_postfix(expr):
	s = stack.Stack(len(expr))
	expr = expr.split()
	ans = 0
	for i in range(len(expr)):
		if expr[i] != '+' and expr[i] != '-' and expr[i] != '*' and expr[i] != '/': 
			s.push(float(expr[i]))
		else:
			val2 = s.pop()
			val1 = s.pop()
			if expr[i] == '+':
				ans = val1 + val2
			elif expr[i] == '-':
				ans = val1 - val2
			elif expr[i] == '*':
				ans = val1 * val2
			elif expr[i] == '/':
				ans = val1 / val2

			

			s.push(ans)	
	return ans

def main():
	print "Hello World"
	expr = '2 3 + 6 9 - 6 / * 8 +'
	print evaluate_postfix_in_switch(expr)
	expr = '2 3 + 6 9 - 5 / * 8 +'
	print evaluate_postfix(expr)

if __name__ == '__main__':
	main()
