
'''arr  có n số :a1,....,aN.nghịch thế là cặp số u và v
sao cho u< v và aU > aV

def solve(arr):
	arr = list(arr)
	count = 0
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]>arr[j]:
				count +=1
	return count
arr = [51,61,76,56,99,98,86]
print(solve(arr))		
'''
def isPrime(prime):
	if prime <2:
		return False
	elif prime ==2:
		return 2
	else:
		for i in range(2,prime):
			if prime % i == 0:
				return False
		return True
n = int(input("enter last element:"))
for i in range(1,n):
	b= i
	while isPrime(b)==True:
		b =(b//10)
	if b == 0:
		print(i,end=" ")

