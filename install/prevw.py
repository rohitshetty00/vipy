def PREVIEW(name,precount,sh):
	f=open("exe.sh",'w')
	f.write("#!/usr/bin/env bash\n")
	f.write("setterm -term linux -back blue -fore default \n")
	f.write("\n clear\n")
	f.write("echo ")
	f.write(name)
	f.write("\necho \n") 
	f.write("\ncat ")
	f.write(name)
	f.write("\nread ")
	f.close()
	from os import*
	system("chmod a+x exe.sh")
	system("gnome-terminal --geometry 50x100+{0}+0 -e ./exe.sh".format(sh))
	
		
		
	
