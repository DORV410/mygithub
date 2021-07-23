def bubsort(ilist):
	for i in range(len(ilist)-1,0,-1):
		for j in range(i):
			if ilist[j] > ilist[j+1]:
				temp = ilist[j]
				ilist[j] = ilist[j+1]
				ilist[j+1] = temp
my_list = []
n = int(input("nhap vao so phan tu trong danh sach:"))
print("nhap vao danh sach cac so: ")
for i in range(n):
	x = int(input())
	my_list.append(x)
bubsort(my_list)
print(my_list)