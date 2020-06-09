from random import randint

x = randint(int(input("Enter the lower bound : ")), int(input("Enter the upper bound : ")))
print("Enter characters to stop the game:")
try:
	y = int(input("Guess the number : "))
except:
	exit()
score = 0

while(y != x):
	score += 1
	if(y > x):
		print("Number is Lower")
	else:
		print("Number is Greater")
	y = int(input("Guess the number : "))
else:
	print("Wow, Correct")
	print("Completed in {:d} attempts".format(score))
