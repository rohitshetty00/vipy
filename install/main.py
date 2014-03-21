#!/usr/bin/env python
from logic import *
from Tkinter import *   
from wfile import* 
from os import*  
from prevw import*    
from license import*    
global root
global name
global precount
precount=1
global number,char,datatype
global string
def CREATFILE():
	global string
	global interact
	interact=Toplevel()
	interact.title("Enter name")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter the file name:").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=CREATFILE_DESTROY).place(x=40,y=50)
	
def CREATFILE_DESTROY():
	global string
	global interact
	global name
	interact.destroy()
	name=string.get()
	name=name+".py"
	CREATEFILE_LOGIC(name)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	mes="\tfile",name,"created"
	s=Label(msg,text=mes,fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
	
def TEXT_VAR():
	global interact
	global number,char
	interact=Toplevel()
	number = IntVar()
	char=IntVar()
	interact.title("variable?")
	interact.geometry("250x100+10+100")
	check= Checkbutton(interact, text="statement", command=PRINT_STATEMENT).place(x=0,y=0)
	check2= Checkbutton(interact, text="variable", command=PRINT_VAR).place(x=100,y=0)	
#
def PRINT_VAR():
	global string
	global interact
	interact.destroy()
	interact=Toplevel()
	interact.title("Enter statement")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter the Variable").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=VARTRANSFER).place(x=40,y=50)
	

def VARTRANSFER():
	global string
	global interact
	interact.destroy()
	name=string.get()
	VARIABLEPRINT_LOGIC(name,root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tvariable statement written",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)

def PRINT_STATEMENT():
	global string
	global interact
	interact.destroy()
	interact=Toplevel()
	interact.title("Enter statement")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter the statement:").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=STATEMENT_TRANSFER).place(x=40,y=50)
	

def STATEMENT_TRANSFER():
	global string
	global interact
	interact.destroy()
	name=string.get()
	STATEMENTPRINT_LOGIC(name,root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tstatement written",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)

def INPUTDATATYPE():
	global interact
	global number,char
	interact=Toplevel()
	number = IntVar()
	char=IntVar()
	interact.title("variable?")
	interact.geometry("250x100+10+100")
	check= Checkbutton(interact, text="number",variable=number, command=VARIABLE_CONDITION).place(x=0,y=0)	
	check2= Checkbutton(interact, text="character",variable=char, command=VARIABLE_CONDITION).place(x=50,y=0)
def VARIABLE_CONDITION():
	global number,char,datatype
	global interact
	global string
	if number.get()==0:
		datatype=0
	else:
		datatype=1
	string =StringVar("")
	interact.destroy()
	interact=Toplevel()
	interact.title("Enter Variable")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter variable:").place(x=0,y=10)
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=TRANSFER_).place(x=40,y=50)
def TRANSFER_():
	global string
	global number,char,datatype
	global interact
	interact.destroy()
	INPUT1(string.get(),datatype,root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tinput taken",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def IF():
	global interact
	global string
	interact=Toplevel()
	interact.title("Enter condition")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter Condition:").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=CON_TRANSFER).place(x=40,y=50)

def CON_TRANSFER():
	global interact
	global string
	cond=string.get()
	print cond
	IF_LOGIC(cond,root.winfo_screenheight(),root)
	interact.destroy()
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tIf starts",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def ELSE():
	ELSE_LOGIC(root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tElse starts",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def END_IF():
	END_IF_LOGIC(root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tIf ends",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def WHILE():
	global interact
	global string
	interact=Toplevel()
	interact.title("Enter condition")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter Condition:").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=WHILE_TRANSFER).place(x=40,y=50)

def WHILE_TRANSFER():
	global interact
	global string
	cond=string.get()
	print cond
	WHILE_LOGIC(cond,root.winfo_screenheight(),root)
	interact.destroy()
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tWhile loop begins",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def END_WHILE():	
	END_WHILE_LOGIC(root.winfo_screenheight(),root)
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\tWhile ends",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def END():
	name=END_LOGIC(root.winfo_screenheight())
	name=name+"\t created"
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text=name,fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)

def STAT():
	global interact
	global string
	interact=Toplevel()
	interact.title("Enter logic")
	interact.geometry("350x100+10+100")
	s=Label(interact,text="Enter logic:").place(x=0,y=10)
	string =StringVar("")
	Entry(interact, width=20, textvariable=string).place(x=150,y=10)
	EnButton=Button(interact,text="Enter",bg="sky blue",width=10,height=2,command=STAT_TRANSFER).place(x=40,y=50)
def STAT_TRANSFER():
	global interact
	global string
	cond=string.get()
	print cond
	LOGIC_LOGIC(cond,root.winfo_screenheight(),root)
	interact.destroy()
	msg=Toplevel()
	msg.geometry("250x100+10+100")
	s=Label(msg,text="\t logic written",fg="blue").place(x=0,y=10)
	EnButton=Button(msg,text="OK",bg="sky blue",width=10,height=2,command=msg.destroy).place(x=20,y=50)
def EXE():
	EXE_LOGIC(root.winfo_screenheight())

def PRE():
	global name
	global precount
	PREVIEW(name,precount,root.winfo_screenheight())
	precount=precount+1

root = Tk()  
root.configure(background="white")
root.resizable(0,0)
root.title("VyAs")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="How to code")
syn=Menu(helpmenu)
helpmenu.add_cascade(label="about syntax ",menu=syn)
syn.add_command(label="Declaration")
syn.add_command(label="array")
syn.add_command(label="use of : for loops,branches")
syn.add_command(label="IF")
syn.add_command(label="Else")
syn.add_command(label="FOR")
syn.add_command(label="WHILE")
syn.add_command(label="Ending loop")
syn.add_command(label="Printing statement")
syn.add_command(label="asking input")
syn.add_command(label="logical operators")
about = Menu(menu)
menu.add_cascade(label="ABOUT",menu=about)
about.add_command(label="license",command=lic)
about.add_command(label="developer")


s=Label(root,text="This is text &interactive field",font="Times,BOLD,U",bg="white",fg="blue").place(x=10,y=100)


CREATFILE=Button(root,text="Start",bg="sky blue",fg="black",width=15,height=5,command=CREATFILE).place(x=0,y=200)
dec=Button(root,text="If",bg="sky blue",width=15,height=5,command=IF).place(x=0,y=285)
array=Button(root,text="End for",bg="sky blue",width=15,height=5).place(x=0,y=370)
ask=Button(root,text="Array\nDeclare",bg="sky blue",width=15,height=5).place(x=0,y=455)
prnt=Button(root,text="Declare",bg="sky blue",width=15,height=5).place(x=145,y=200)
pif=Button(root,text="Else",bg="sky blue",width=15,height=5,command=ELSE).place(x=145,y=285)
pelse=Button(root,text="While",bg="sky blue",width=15,height=5,command=WHILE).place(x=145,y=370)
pfor=Button(root,text="Correct",bg="sky blue",width=15,height=5).place(x=145,y=455)
pwhile=Button(root,text="Print",bg="sky blue",width=15,height=5,command=TEXT_VAR).place(x=290,y=200)
preview=Button(root,text="Endif",bg="sky blue",width=15,height=5,command=END_IF).place(x=290,y=285)
endif=Button(root,text="End while",bg="sky blue",width=15,height=5,command=END_WHILE).place(x=290,y=370)
endfor=Button(root,text="Preview",bg="sky blue",width=15,height=5,command=PRE).place(x=290,y=455)
endelse=Button(root,text="Input",bg="sky blue",width=15,height=5,command=INPUTDATATYPE).place(x=435,y=200)
endwhile=Button(root,text="For",bg="sky blue",width=15,height=5).place(x=435,y=285)
logic=Button(root,text="Statement",bg="sky blue",width=15,height=5,command=STAT).place(x=435,y=370)
stop=Button(root,text="End",bg="sky blue",width=15,height=5,command=END).place(x=435,y=455)
prina=Button(root,text="Execute",bg="sky blue",width=30,height=4,command=EXE).place(x=150,y=543)
root.mainloop()
