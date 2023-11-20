#点击上一张、下一张显示图片
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import os
count=1
def get_image_files(directory):
    image_files = []
    for file in os.listdir(directory):
        if file.endswith(".png"):
            image_files.append(file)
    return image_files




def up():
    global count
    count += 1
    if count > listlen-1:
        count = 0
    img = Image.open(path+'\\' +image_files[count])
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    with open('result.txt', encoding='utf-8') as f:
        text = f.read()
        f.close()
    resultch=text.index(image_files[count])
    tk.Label(text=resultch)


def down():
    global count
    count-=1
    if count<0:
        count=listlen-1
    img = Image.open(path +'\\'+image_files[count])
    img = img.resize((576, 324), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    with open('result.txt', encoding='utf-8') as f:
        text = f.read()
        f.close()
    resultch=text.index(image_files[count])
    tk.Label(text=resultch)

root=tk.Tk()
root.title('相册')
path=r'D:/img/'
image_files = get_image_files(path)
print(image_files[0])
listlen: int=len(image_files)
print(listlen)
tk.Label(root, width=40, height=3, wraplength=80)
img=Image.open(path+'\\'+image_files[0])
img = img.resize((576, 324), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
box=Frame(root, width=600,height=400,borderwidth=5)
box.grid(row=0, column=0)
label=Label(box,width=600,height=337,image=img)
label.grid(row=0,columnspan=2)
btnup=Button(box,text="上一张", command=up)
btndown=Button(box,text="下一张", command=down)
btnup.grid(row=1, column=0)
btndown.grid(row=1, column=1)
root.mainloop()
