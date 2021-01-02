import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import pandas as pd
window = tk.Tk()
window.title("concat")
fontStyle = tkFont.Font(family="Ink Free", size=100)
fontstyle2 = tkFont.Font(family = "Arial",size=30)
canvas = tk.Canvas(window,width=500,height=500)
canvas.grid(columnspan=3,rowspan=3)
v = IntVar()
v.set(1)
def button():
    print(v.get())
def openfile():
    file = askopenfile(parent=window,mode="rb",title="choose a file",filetype=[("excel file",".xlsx")])
    if file:
        global a
        a=pd.read_excel(file)
        tk.Label(window,text="successful",fg="black",bg="green").grid(column=2,row=1)
def openfile2():
    file = askopenfile(parent=window,mode="rb",title="choose a file",filetype=[("excel file",".xlsx")])
    if file:
        global b
        b= pd.read_excel(file)
        tk.Label(window,text="successful",fg="black",bg="green").grid(column=2,row=2)
        messagebox.showinfo("enter the title of the file","enter the file's title in the box below")

tk.Label(window,text="concat",font=fontStyle,fg="black",bg="green").grid(column=2,row=0)
tk.Button(window,text="first file",bg="green",fg="black",width=8,command=openfile).grid(column=0,row=1)
tk.Button(window,text="second file",bg="green",fg="black",width=8,command=openfile2).grid(column=0,row=2)
rad1 = tk.Radiobutton(window,text="row",value=0,variable=v,command=button).grid(column=3,row=2)
rad2 = tk.Radiobutton(window,text="column",value=1,variable=v,command=button).grid(column=3,row=1)
x = tk.Entry(window)
x.grid(column=1,row=3)
tk.Label(window,text="enter title of new file",bg="green",fg="black",width=20).grid(column=2,row=3)


def concat():
    d = x.get()
    c = pd.concat([a,b],axis=v.get())
    c.to_excel(d+".xlsx",index=False)
    
    messagebox.showinfo("success","your file has been created successfully in the name "+d)
tk.Button(window,text="combine",fg="black",bg="green",command=concat,width=10).grid(column=3,row=3)


