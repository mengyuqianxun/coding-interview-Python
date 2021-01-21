#全面但不够高效的解法
def power1(base,exponent):
	if base == 0:
		if exponent < 0:
			print('底数为0，指数为负，错误')
			return
		else:
			return 0
	else:
		if exponent == 0:
			return 1
		elif exponent > 0:
			result = 1
			for i in range(exponent):
				result *= base
			return result
		else:
			result = 1
			for i in range(-exponent):
				result *= base
			return 1/result

#全面且高效的解法
def power2(base,exponent):
	if base == 0:
		if exponent < 0:
			print('底数为0，指数为负，错误')
			return
		else:
			return 0
	else:
		if exponent == 0:
			return 1
		elif exponent > 0:
			result = power_postive_exponent(base,exponent)
			return result
		else:
			result = power_postive_exponent(base,-exponent)
			return 1/result

def power_postive_exponent(base,exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	result = power_postive_exponent(base,exponent>>1)
	result *= result
	if exponent & 0x1 == 1:
		result *= base
	return result

if __name__ == '__main__':
	result1 = power1(2,-3)
	print(result1)
	result2 = power2(2,10)
	print(result2)
