from sympy import *

m = int(input("Array rows : "))
n = int(input("Array cols : "))
def create(m, n):
	l = []
	for i in range(0, m):
		for j in range(0, n):
			try:
				l.append(int(input("a[%d][%d] : " % (i, j))))
			except:
				print("Try again")
				l.append(int(input("a[%d][%d] : " % (i, j))))
	return l
print("Enter constant matrix : ")
C = Matrix(m, 1, create(m, 1))
print("Enter coefficient matrix : ")
A = Matrix(m, n, create(m, n))
try:
	print(A.LUsolve(C))
except:
	print("Unsolvable")
