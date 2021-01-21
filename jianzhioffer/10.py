#递归方法，效率很差，num = 100时候就很明显慢
def fib1(num):
	if num <= 0:
		return 0
	if num == 1:
		return 1
	return (fib1(num-1) + fib1(num-2))

def fib2(num):
	a,b = 0,1
	for i in range(num):
		yield b
		a,b = b,a+b

if __name__ =="__main__":
	print(fib1(10))
	num = 100
	f = fib2(num)
	for i in range(num-1):
		next(f)
	print(next(f))
