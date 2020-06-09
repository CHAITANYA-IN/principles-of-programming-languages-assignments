l = []
lint = []
i = 0
x = int(input("Enter the total no. of pages : "))
pages = []

while input("Still Existing Pages ! 'Y' for Yes : ") == "Y":
	l.append(input("Enter page range or numbers : "))
	i += 1

for i in l:
	try:
		lint.append(int(i))
	except:
		a = i.index("-")
		lint += range(int(i[:a]), int(i[a+1:])+1)

i = 0
while i < len(lint):
	if(lint[i] > x):
		lint.remove(lint[i])
		i -= 1
	i += 1

for i in range(1, x+1):
	if(not i in lint):
		pages.append(i)

print("Missing Pages : ", pages)
