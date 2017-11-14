from tkinter import *
import record as auto_record
from tkinter import messagebox



class MyGui :
    global this
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.minsize(width=410, height=300)
        master.maxsize(width=410, height=300)
        self.menu()
        self.content()



    def menu(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda:self.new_file(None), accelerator="Ctrl+N")
        filemenu.add_command(label="Open", command=lambda:self.open_file(None), accelerator='Ctrl+O')
        filemenu.add_command(label="Save", command=lambda:self.save_file(None), accelerator='Ctrl+S')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda:self.exit(None), accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=filemenu)

        editMenu = Menu(menubar, tearoff=0)
        editMenu.add_command(label="Play", command=lambda:self.auto_play(None), accelerator="Ctrl+F1")
        editMenu.add_command(label="Pause", command=lambda:self.auto_pause(None), accelerator="Ctrl+F2")
        editMenu.add_command(label="POS", command=lambda: self.position(None), accelerator="F2")
        editMenu.add_command(label="REC", command=lambda: self.rec(None), accelerator="F3")
        editMenu.add_command(label="REC_STOP", accelerator="F4")
        menubar.add_cascade(label="Edit", menu=editMenu)

        self.master.config(menu=menubar)
        self.master.bind('<Control-q>', self.exit)
        self.master.bind('<Control-o>', self.open_file)
        self.master.bind('<Control-F1>', self.auto_play)
        self.master.bind('<Control-F2>', self.auto_pause)
        self.master.bind('<F2>', self.position)
        self.master.bind('<F3>', self.rec)

    def content(self):

        self.sc = Scrollbar(root)
        self.line = Text(root, height=20, width=28)
        self.sc.grid(column=1, row=0, rowspan=6, sticky=N+S+W, pady=10)
        self.line.grid(row=0, column=0, rowspan=6, sticky='E', pady=10, padx=(10, 0))
        self.sc.config(command=self.line.yview)
        self.line.config(yscrollcommand=self.sc.set)
        self.line.insert(END, 0.5)

        self.l1 = Label(root, text="X : 0    Y: 0", width=20, anchor="center")
        self.l1.grid(row=0, column=2, columnspan = 4, padx=5)

        self.lX = Label(root, text="X : ", width=5, anchor="n")
        self.lX.grid(row=1, column=2)
        self.tX = Text(root, width=5, height=1)
        self.tX.grid(row=1, column=3)


        self.lY = Label(root, text="Y : ", width=5, anchor="ne")
        self.lY.grid(row=1, column=4)
        self.tY = Text(root, width=5, height=1)
        self.tY.grid(row=1, column=5)

        self.lD = Label(root, text="Delay : ", width=10, anchor="nw")
        self.lD.grid(row=2, column=2, columnspan=2)
        self.tD = Text(root, width=10, height=1)
        self.tD.insert(END, 0.5)
        self.tD.grid(row=2, column=4, columnspan=2)

        self.bI = Button(root, text="Insert", command=self.insert, width=10)
        self.bI.grid(row=3, column=2, columnspan=4)

        self.lL = Label(root, text="Loop : ", width=10, anchor="nw")
        self.lL.grid(row=5, column=2, columnspan=2)
        self.tL = Text(root, width=10, height=1)
        self.tL.insert(END, 1)
        self.tL.grid(row=5, column=4, columnspan=2)

    def new_file(self, event=None):
        print("new File!")

    def open_file(self, event=None):
        print('open file')

    def save_file(self, event=None):
        print('save file')

    def exit(self, event=None):
        self.master.destroy()

    def auto_play(self, event=None):
        print('play')

    def auto_pause(self, event=None):
        print('pause')

    def position(self, evnet=None):
        x = self.master.winfo_pointerx()
        y = self.master.winfo_pointery()
        abs_coord_x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        abs_coord_y = self.master.winfo_pointery() - self.master.winfo_rooty()
        self.tX.delete(1.0, END)
        self.tY.delete(1.0, END)
        self.tX.insert(END,str(x))
        self.tY.insert(END,str(y))

    def movePos(self, event):
        print(str(event.x_root) + ',' +str(event.y_root))

    def insert(self):
        print('click me')

    def rec(self, evnet=None):
        auto_rec = auto_record.record(self)
        self.record_confirm()

    def record_confirm(self):
        print(1)
        result = messagebox.askquestion("녹화", "녹화파일을 불러오시겠습니까?")
        if result:
            self.line.delete(1.0, END)
            self.line.insert(END, self.data)
        else:
            print('false')


root = Tk()
my_gui = MyGui(root)

root.mainloop()
