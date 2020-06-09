import math
n = 1
m = 0
sum = 0
t = 0

while t < 10:
	m = 0
	i = 1
    for i in range(n, 1):
        if(n % i == 0):
            
    
	for i in range(1, int(math.sqrt(n))):
		if(n % i == 0):
            if(n // i == i):
                m += i
            else:
                m = m +
	sum = 0
	for i in range(1, m):
		if(m % i == 0):
			sum += i
	if(sum == n and n >= m):
		print(m, n)
		t += 1
	n += 1
