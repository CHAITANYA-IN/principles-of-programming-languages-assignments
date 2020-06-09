import os

link = input("Enter a link(like this : 'facebook.com') : ")

f = open("/etc/hosts", "rt")
content = f.read()

w = open("hosts", "a+")
w.write(content)

if(link not in f.read()):
	w.write("127.0.0.1\t" + link)
	w.write("\n127.0.0.1\twww." + link)

f.close()
w.close()

os.system("sudo mv ./hosts /etc/hosts")
