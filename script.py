from __future__ import unicode_literals
import tkinter
from tkinter import *
from PIL import ImageTk,Image
import os

tk = Tk()

bg = Image.open("background2.jpg")
bg_lbl = ImageTk.PhotoImage(bg)
label = Label(image=bg_lbl)
label.image = bg_lbl
label.place(relheight=1,relwidth=1)

class GUI_TK:
    def __init__(self,master):
        self.master = master
        self.master.title("Playlist Maker")
        self.master.iconbitmap("favicon.ico")
        self.master.geometry("800x600")

        self.label = Label(text="Enter the file name: ",font="IMPRISHA 12")
        self.label.pack(pady="3")

        self.entry = Entry(width=30)
        self.entry.pack(pady="8")

        self.button = Button(text="Download", command=lambda: download(),pady="3",padx="3",activebackground="gray",activeforeground="white")
        self.button.pack(pady="10")

def download():
    raise SystemExit

gui = GUI_TK(tk)

tk.resizable(height=False,width=False)
tk.mainloop()