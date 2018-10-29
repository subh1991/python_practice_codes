def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num - 1)

def fibonacci(num):
	if num<=0:
		return 0
	elif num == 1:
		return 0
	elif num == 2:
		return 1
	else:
		return fibonacci(num-1) + fibonacci(num-2)
		
def pallindrom(s):
	if len(s) <= 1:
		return True
	if s[0] == s[-1]:
		return pallindrom(s[1:-1])
	else:
		return False
	

def main1():
	print "Hello World"
	print "give an input for factorial: "
	num = int(raw_input())
	fac = factorial(num)
	print "Factorial of ", num, " is: ",fac

	print "give an input for fibonacci Series: "
	num = int(raw_input())
	fib = fibonacci(num)
	print num,"th fibonacci number is: ", fib

def main1():
	print "Enter something to check if pallindrom:"
	s = str(raw_input())
	if pallindrom(s):
		print s, " is pallindrom"
	else:
		print s, " is not pallindrom"

def main():
	print "Enter a number:"
	num = list(str(raw_input()))
	num.append(num[0])
	small_num = [num[0]]
#	print num
#	num.insert(-1, num[4])
#	print num
	i=1
	while not pallindrom(num):
		num.insert(-i, num[i])
		small_num.insert(0, num[i])
		i +=1
	print small_num
	res = 0
	for j in range(1, len(small_num)+1):
		res = res + int(small_num[-j]) * (10 **(j-1))
	print res
	

if __name__ == "__main__":
	main()


















