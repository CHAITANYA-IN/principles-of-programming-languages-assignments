y = int(input("Enter Lower Bound : "))
x = int(input("Enter Upper Bound : "))

for i in range(y, x):
	sum = 0
	s = "%d" % i	#s = str(i)
	power = len(s)
	for j in s:
		sum += int(j) ** power
	if(sum == i):
		print(i)
