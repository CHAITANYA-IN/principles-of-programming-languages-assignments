from random import randint

while(True):
	i = input("Roll the dice ? (Y/n) : ")
	if i == 'Y':
		print(randint(1,6))
	elif(i == "n"):
		print("Bye")
		break
	else:
		print("Give Proper Response!")
