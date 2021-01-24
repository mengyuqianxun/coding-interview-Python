import numpy as np

def AgeSort(arr):
	if len(arr) == 0:
		return
	count =[0]*100
	for i in range(len(arr)):
		count[arr[i]] += 1
	age = []
	for i in range(100):
		for j in range(count[i]):
			age.append(i)
	return age

if __name__ == '__main__':
	#size可以设为20000
	index = np.random.randint(20,99,size = 200)
	age = index.tolist()
	age = AgeSort(age)
	print(age)

