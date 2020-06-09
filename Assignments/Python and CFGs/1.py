b1 = ['goat','grass','tiger']
b2 = []
b = ['man']
def val(b):
	if 'grass' and 'tiger' in b:
		return 1
	elif len(b) == 0 or len(b) == 1:
		return 1
	else:
		return 0
i = 0	
while True:
	s = b1[i]
	if len(b) == 2:
		b1.append(b[-1])
		del b[-1]
		print(b1[-1]+",man  \t: bank2 to bank1")
	b.append(s)
	b1.remove(s)
	if (val(b1)):
		b2.append(s)
		b.remove(s)
		print(b2[-1]+", man\t: bank1 to bank2")
		if(not(val(b2)) and len(b2) == 2):
			b.append(b2[0])
			del b2[0]
		elif(len(b2)!=3):
			print("man \t\t: bank2 to bank1")
	else:
		b1.append(s)
		del b[-1]
	if len(b1) == 0 and len(b2) == 3:
		break	
