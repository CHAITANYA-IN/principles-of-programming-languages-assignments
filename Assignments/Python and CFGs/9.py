import math
from statistics import harmonic_mean

n = 1
t = 0
i = 1

while t < 10 :
	l_divisor = []
	i = 1
	while(i <= math.sqrt(n)):
		if(n % i == 0):
			if(n/i == i):
				l_divisor.append(i)
			else:
				l_divisor += [i, int(n/i)]
		i += 1
	har_div = harmonic_mean(l_divisor)
	if(math.floor(har_div) == math.ceil(har_div)):
		print(n)
		t += 1
	n += 1
