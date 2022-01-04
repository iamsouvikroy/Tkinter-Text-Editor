from tkinter import*
from tkinter import filedialog, messagebox, ttk, colorchooser, font


# FileTypes while opening a file
open_filetypes=[
    ('Text Documents(*.txt)', '*.txt'),
    ('All Files', '*.*')
]

# FileTypes while saving a file
saveas_filetypes=[
    ('Text Documents(*.txt)', '*.txt'),
    ('All Files', '*.*') 
]


# Creating a MainWindow class for the window
class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        colortheme = "#00FF00"


        # Open File Function
        def openfile():
            global file, filepath
            filepath = filedialog.askopenfilename(filetypes=open_filetypes)
            file = open(f'{filepath}')
            filecontent = file.read()
            self.textarea.delete(1.0, END)
            self.textarea.insert(1.0, filecontent)
            filename = filepath.split('/')
            actualfilename = filename[len(filename) - 1]
            self.title(f'{actualfilename} - Notepad-Clone by Souvik Roy')
            file.close()


        # Save File Function
        def save():
            try:
                file = open(f'{filepath}', 'w')
                content = self.textarea.get(1.0, END)
                file.write(f'{content}')
            except:
                saveas()


        # SaveAs File Function
        def saveas():
            saveasfile = filedialog.asksaveasfile(filetypes=saveas_filetypes)
            filename = saveasfile.name
            file = open(f'{filename}', 'w')
            content = self.textarea.get(1.0, END)
            file.write(f'{content}')


        # New File Function
        def new():
            pass


        self.title("Untitled - Souvik's Code-Editor")
        self.geometry('600x400')
        self.menubar = Menu(self, bg="#000")
        self.config(bg="blue", menu=self.menubar)

        # ADDING THE MENU BAR ITEMS0

        # File Menu Item
        self.file = Menu(self, tearoff=False) 
        self.menubar.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="New", accelerator="Ctrl+N")
        self.file.add_command(label="New Window          ", accelerator="Ctrl+Shift+N")
        self.file.add_command(label="Open...", accelerator="Ctrl+O", command=openfile)
        self.file.add_command(label="Save", accelerator="Ctrl+S", command=save)
        self.file.add_command(label="Save As...", accelerator="Ctrl+Shift+S", command=saveas)
        self.file.add_command(label="Close", accelerator="Ctrl+")
        self.file.add_separator()
        self.file.add_command(label="Page Setup...")
        self.file.add_command(label="Print...", accelerator="Ctrl+P")
        self.file.add_separator()
        self.file.add_command(label="Exit", command=self.quit)

        # Edit Menu item
        self.edit = Menu(self, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.edit.add_command(label="Undo", accelerator="Ctrl+Z")
        self.edit.add_command(label="Redo", accelerator="Ctrl+Y")
        self.edit.add_separator()
        self.edit.add_command(label="Cut", accelerator="Ctrl+X")
        self.edit.add_command(label="Copy", accelerator="Ctrl+C")
        self.edit.add_command(label="Paste", accelerator="Ctrt+V")
        self.edit.add_separator()
        self.edit.add_command(label="Find", accelerator="Ctrl+F")
        self.edit.add_command(label="Replace     ", accelerator="Ctrl+H")
        
        # View Menu item
        self.view = Menu(self, tearoff=False)
        self.menubar.add_cascade(label="View", menu=self.view)
        self.view.add_command(label="Wrap", accelerator="Ctrl+W")
        self.view.add_checkbutton(label="Status Bar", activebackground="#000")
        
        # Preferences Menu Item
        self.preferences = Menu(self, tearoff=False)
        self.menubar.add_cascade(label="Preferences", menu=self.preferences)
        self.preferences.add_command(label="TextArea Theme")
        self.preferences.add_command(label="Color Theme")


        # ADDING THE WINDOW COMPONENTS

        # 
        self.statusbar = Label(bg="#fcfcfc")
        self.statusbar.pack(side=BOTTOM, fill=X)
        
        # Vertical ScrollBar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Horizontal ScrollBar
        self.horizontalscrollbar = Scrollbar(self, orient="horizontal")
        self.horizontalscrollbar.pack(side=BOTTOM, fill=X)

        # TEXTAREA
        self.textarea = Text(self, bd=0, height=48, yscrollcommand=self.scrollbar.set, xscrollcommand=self.horizontalscrollbar.set, wrap="none", font=('Consolas', 14), foreground="#00ff00", bg="#000000", selectbackground="#3EFF97", selectforeground="#000")
        self.textarea.pack(side=TOP, fill=BOTH)
        self.textarea.configure(insertbackground="#00ff00")

        # Configuring the Scrollbars
        self.scrollbar.config(command=self.textarea.yview)
        self.horizontalscrollbar.config(command=self.textarea.xview, bg="#000")


# RUNNING THE ACTUAL APP
if __name__ == '__main__':
    MainWindow().mainloop()