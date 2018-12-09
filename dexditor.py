import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from pygments import lex
from pygments.lexers import PythonLexer
from main import  *

class Dexditor:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
        		self.__root.wm_iconbitmap("Dexditor.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled - Dexditor")
        self.__thisTextArea.tag_configure("red", foreground="#ff0000")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="New File",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open File",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save As",command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Generate Code", command=self.__exportfile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)


        self.__thisHelpMenu.add_command(label="About Dexditor",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="About",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("Dexditor","Created by: Shamim Ali \nShamimnox@gmail.com")

    def __openFile(self):
        
        self.__file = askopenfilename(initialfile='Untitled.cbd',defaultextension=".cbd",filetypes=[("Dexditor Documents","*.cbd")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Dexditor")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - Dexditor")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.cbd',defaultextension=".cbd",filetypes=[("Dexditor Documents","*.cbd")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                print(str(self.__thisTextArea.get(1.0,END)))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Dexditor")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __exportfile(self):

        self.__saveFile()
        msg = generate_code(self.__file)
        if("error" in msg):
            showerror("Error", msg)
        else:
            showinfo("Success", msg)

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def syn(self,event=None):
        print("hello")
        self.__thisTextArea.mark_set("range_start", "1.0")
        data = self.__thisTextArea.get("1.0", "end-1c")
        for token, content in lex(data, PythonLexer()):
            self.__thisTextArea.mark_set("range_end", "range_start + %dc" % len(content))
            self.__thisTextArea.tag_add(str(token), "range_start", "range_end")
            self.__thisTextArea.mark_set("range_start", "range_end")

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''
        print("ggg")
        start = self.__thisTextArea.index(start)
        end = self.__thisTextArea.index(end)
        self.__thisTextArea.mark_set("matchStart", start)
        self.__thisTextArea.mark_set("matchEnd", start)
        self.__thisTextArea.mark_set("searchLimit", end)

        count = tkinter.IntVar()
        while True:
            print("hello")
            index = self.__thisTextArea.search(pattern, "matchEnd", "searchLimit",
                                count=count, regexp=r'not')
            print(index)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            self.__thisTextArea.mark_set("matchStart", index)
            self.__thisTextArea.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.__thisTextArea.tag_add(tag, "matchStart", "matchEnd")

    def run(self):
        #self.__root.bind("<KeyRelease>", self.syn())
        #run main application
        self.__root.mainloop()

class gogo:
    def run(self):
        notepad = Dexditor(width=800, height=600)
        notepad.run()




