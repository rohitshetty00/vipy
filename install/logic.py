from tes import*
global name
global tab
global count
programfile=[]
viewfile=[]
count=0
global programfile,viewfile,count
def CREATEFILE_LOGIC(nam):
	global name
	global tab
	tab=0
	name=nam
	f=open(nam,'w')
	f.close()
def VARIABLEPRINT_LOGIC(stat,sh,root):
	global programfile,viewfile,count	
	global tab
	TAB(tab)
	programfile.append('print ')
	programfile.append(stat)
	programfile.append("\n")
	viewfile.append('print '+stat+'\n') 
	VIEW_LOGIC(sh,root)
	count=count+1
def STATEMENTPRINT_LOGIC(sta,sh,root):
	global programfile,viewfile,count	
	global tab
	TAB(tab)
	programfile.append('print ')
	programfile.append('\"')
	programfile.append(sta)
	programfile.append('\"')
	programfile.append("\n")
	viewfile.append('print '+'\"'+sta+'\"'+'\n')
	 
	VIEW_LOGIC(sh,root) 
	count=count+1
def INPUT1(nam,data,sh,root):
	global programfile,viewfile,count
	global tab
	TAB(tab)	
	if data==1:
		programfile.append(nam)
		programfile.append(" = input()")
		viewfile.append(nam+" = input()")
	else:
		programfile.append(nam)
		programfile.append(" = raw_input()")
		viewfile.append(nam+" =raw_input()")
	programfile.append("\n")
	viewfile.append('\n')
	VIEW_LOGIC(sh,root)
	count=count+1 
	 
def IF_LOGIC(CON,sh,root):
	global tab
	global programfile,viewfile,count
	TAB(tab)
	programfile.append("if ")
	programfile.append(CON)
	programfile.append(" :")
	programfile.append("  \t\t\t# if starts")
	programfile.append("\n")
	viewfile.append("if "+CON+" :\t\t\t#if starts"+'\n')
	VIEW_LOGIC(sh,root) 
	count=count+1
	tab=tab+1
def ELSE_LOGIC(sh,root):
	global programfile,viewfile,count
	TAB(tab-1)
	programfile.append("else: \t\t\t#else starts\n")
	programfile.append("\n")
	viewfile.append("else: \t\t\t# else starts\n")
	VIEW_LOGIC(sh,root)
	count=count+1
def END_IF_LOGIC(sh,root):
	global tab
	global programfile,viewfile,count
	tab=tab-1
	programfile.append("\n ")
	viewfile.append('\n')
	TAB(tab)
	programfile.append("#if ends \n ")
	viewfile.append('#if ends \n')
	VIEW_LOGIC(sh,root)
	count=count+1 	
def WHILE_LOGIC(CON,sh,root):
	global tab
	global programfile,viewfile,count
	TAB(tab)
	programfile.append("while ")
	programfile.append(CON)
	programfile.append(":")
	programfile.append("\t\t\t# while begins\n")
	viewfile.append('while '+CON+":"+"\t\t\t# While begins"+'\n')
	VIEW_LOGIC(sh,root)
	count=count+1 	
	tab=tab+1
def END_WHILE_LOGIC(sh,root):
	global programfile,viewfile,count,tab
	tab=tab-1
	programfile.append("\n")
	viewfile.append('\n')
	TAB(tab)
	programfile.append("#while ends\n")
	viewfile.append('#while ends\n')
	VIEW_LOGIC(sh,root)
	count=count+1 
	
def LOGIC_LOGIC(CON,sh,root):
	global tab
	global programfile,viewfile,count
	TAB(tab)
	programfile.append(CON)
	programfile.append("\n")
	viewfile.append(CON+"\n")
	VIEW_LOGIC(sh,root)
	count=count+1 
	
def VIEW_LOGIC(sh,root):
	i=0
	global programfile,viewfile,count,name
	f=open("viewfile.txt",'w')
	while (i<len(viewfile)):
		f.write(viewfile[i])
		i=i+1
	f.close()
	ho(count,sh,root)
def END_LOGIC(sh):
	i=0
	global programfile,viewfile,count,name
	f=open(name,'w')
	f.write("\t\t\t#begins\n\n")
	while (i<len(programfile)):
		f.write(programfile[i])
		i=i+1
	f.write("\n\t\t\t#END")
	f.write("\nstop=input()#neglect this")
	f.close()
	return name

def EXE_LOGIC(sh):
	f=open("exe.sh",'w')
	f.write("\t\t\t#!/usr/bin/env bash\n")
	f.write("setterm -term linux -back blue -fore default \n")
	f.write("clear\n")
	f.write("echo \"\nexecution begins....\"\n")
	f.write("python ")
	f.write(name)	
	f.close()
	from os import*
	system("chmod a+x exe.sh")
	system("gnome-terminal --geometry 50x100+{0}+0 -e ./exe.sh".format(sh))
def TAB(tablocal):	
	global programfile,viewfile,count	
	while(tablocal!=0):
		print tablocal
		programfile.append('\t')
		viewfile.append('\t')
		tablocal=tablocal-1
