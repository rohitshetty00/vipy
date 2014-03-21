def lic():
	f = open('list' , 'r')
	s=f.read()
	f.close()
	fp=open('c.sh','w')
	fp.write("cd ")
	fp.write(s)
	fp.write("gedit lic.txt")
	fp.close()
	from os import*

	system("bash c.sh")
	print "ok"
