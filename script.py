from __future__ import unicode_literals
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image

tk = Tk()

# bg = Image.open("background2.jpg")
# bg_lbl = ImageTk.PhotoImage(bg)
# label = Label(image=bg_lbl)
# label.image = bg_lbl
# label.place(relheight=1,relwidth=1)

class GUI_TK:
    def __init__(self,master):
        self.master = master
        self.master.title("Playlist Maker")
        self.master.iconbitmap("favicon.ico")
        self.master.geometry("800x600")

        self.file_label = Label(text="Browse file :")
        self.file_label.pack(pady="3")
        self.file_button = Button(text="Select", command=self.readFile)
        self.file_button.pack(pady="8")

        self.path_label = Label(text="Choose file destination :")
        self.path_label.pack(pady="8")
        self.path_button = Button(text="Select", command=self.pathSelect)
        self.path_button.pack(pady="8")

        self.download_button = Button(text="Download",pady="3",padx="3",activebackground="gray",activeforeground="white")
        self.download_button.pack(pady="10")

    def readFile(self):
        filePath = askopenfile(mode='r',filetypes=[("all files","*.*")])
        self.file_label.config(text=filePath)

    def pathSelect(self):
        path = filedialog.askdirectory()
        if(path):
            self.path_label.config(text=path)


def download():
    raise SystemExit

gui = GUI_TK(tk)

tk.resizable(height=False,width=False)
tk.mainloop()