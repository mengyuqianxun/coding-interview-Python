def MaxSubstrLen(s):
	tmp = ''
	l,f = 0,0
	for i in range(len(s)):
		if s[i] not in tmp:
			f += 1
			tmp += s[i]
		else:
			index = tmp.find(s[i])
			f = len(tmp) - index
			tmp = tmp[index + 1:] + s[i]
		if f > l:
			l = f
	return l

if __name__ == '__main__':
	sList = ['arabcacfr','arabcafr','aaaaa','abcdefg','mnkabca']
	for s in sList:
		l = MaxSubstrLen(s)
		print(l,end=' ')