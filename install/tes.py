from Tkinter import*
roottop=[]
def ho(tim,sh,root):
	if tim>0:
		roottop[tim-1].destroy()
	for i in range(1):	
		f=open("viewfile.txt",'r')
		s=f.readline()
		roottop.append(Toplevel())
		roottop[tim].title("Inter")
		roottop[tim].geometry("400x{0}+{0}+0".format(sh))
	
		text = Text(roottop[tim], height=root.winfo_screenwidth(),width=root.winfo_screenheight())
		scroll = Scrollbar(roottop[tim], command=text.yview)
		text.configure(yscrollcommand=scroll.set)
		text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
		text.tag_configure('big', font=('Verdana', 24, 'bold'))
		text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
		text.tag_configure('groove', relief=GROOVE, borderwidth=2)
		while s!='':
	
			text.insert(END,s)
			s=f.readline()
		text.pack(side=LEFT)
		scroll.pack(side=RIGHT, fill=Y)
		f.close()		
		return
		
