def FlipWord(s):
	strList = s.split(' ')
	reslut = ' '.join(strList[::-1])
	return reslut

if __name__ == '__main__':
	sList = ['I am a student.','',' ','word']
	for s in sList:
		reslut = FlipWord(s)
		print(reslut)


