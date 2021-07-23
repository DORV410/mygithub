'''
Bài 1: Tính S(n) = 1 + 2 + 3 + … + n
Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2
Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n
Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n
Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)

Bài 6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)
Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1
Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2
Bài 9: Tính T(n) = 1 x 2 x 3…x N
Bài 10: Tính T(x, n) = x^n

Bài 11: Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N
Bài 12: Tính S(n) = x + x^2 + x^3 + … + x^n
Bài 13: Tính S(n) = x^2 + x^4 + … + x^2n
Bài 14: Tính S(n) = x + x^3 + x^5 + … + x^2n + 1
Bài 15: Tính S(n) = 1 + 1/1 + 2 + 1/ 1 + 2 + 3 + ….. + 1/ 1 + 2 + 3 + …. + N

Bài 16: Tính S(n) = x + x^2/1 + 2 + x^3/1 + 2 + 3 + … + x^n/1 + 2 + 3 + …. + N
Bài 17: Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!
Bài 18: Tính S(n) = 1 + x^2/2! + x^4/4! + … + x^2n/(2n)!
Bài 19: Tính S(n) = 1 + x + x^3/3! + x^5/5! + … + x^(2n+1)/(2n+1)!
Bài 20: Liệt kê tất cả các “ước số” của số nguyên dương n

Bài 21: Tính tổng tất cả các “ước số” của số nguyên dương n
Bài 22: Tính tích tất cả các “ước số” của số nguyên dương n
Bài 23: Đếm số lượng “ước số” của số nguyên dương n
Bài 24: Liệt kê tất cả các “ước số lẻ” của số nguyên dương n
Bài 25: Tính tổng tất cả các “ước số chẵn” của số nguyên dương n

Bài 26: Tính tích tất cả các “ước số lẻ” của số nguyên dương n
Bài 27: Đếm số lượng “ước số chẵn” của số nguyên dương n
Bài 28: Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó
Bài 29: Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ lớn nhất là 25
Bài 30: Cho số nguyên dương n. Kiểm tra xem n có phải là số hoàn thiện hay không


'''
def sum1():
	n = int(input("nhap vao so n: "))
	i = 1
	S = 0
	while (i <= n ):
		S = S + i*i
		i +=1
	return S
def sum2():
	n = int(input("Nhap vao so n: "))
	print("Sum of array S(n) = 1 + 1/2 + 1/3 + … + 1/n:")
	i =1 
	S= 0 
	while( i <= n ):
		S = S + 1/i
		i +=1
	return S
def sum3():
	n = int(input(" nhap vao so n:"))
	print("S(n) = ½ + ¼ + … + 1/2n\n")
	i =1
	S = 0
	while (i <= n):
		k = int(2*i)
		S = S + 1/k
		i +=1
	return S
'''def sum4(n):
	while n == 0:
		return 1 
	return sum4(n-1)+1/((2*n)+1) 
print(sum4(10)-1)'''
def sum4():
	n = int(input())
	i = 1
	S = 0
	while (i<= n):
		S = S+ 1/((2*i)+1)
		i+=1
	return S

