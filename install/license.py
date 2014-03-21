from Tkinter import *
def LIC():
	f=open("lic.txt",'r')
	s=f.readline()
	root = Tk()
	root.title("license")
	root.geometry("%dx%d+%d+0"%(root.winfo_screenwidth(),root.winfo_screenheight(),root.winfo_screenwidth()))
	
	text = Text(root, height=root.winfo_screenwidth(),width=root.winfo_screenheight())
	scroll = Scrollbar(root, command=text.yview)
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
	root.mainloop() 
	f.close()
