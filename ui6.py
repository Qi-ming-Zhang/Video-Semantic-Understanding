#点击上一张、下一张显示图片
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import os
from pathlib import Path

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
    print(path+'\\' +image_files[count])
    img = Image.open(path+'\\' +image_files[count])
    img = img.resize((576, 324), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    check_path=Path(image_files[count]).name
    with open(r'result.txt', 'r', encoding='utf8') as f:
        text = f.readlines()
    for i in range(len(text)):
        if check_path+'\n' == text[i]:
            print()
            resultch=text[i + 1]+'\n'+text[i + 2]+'\n'+text[i + 3]
    print(resultch)

    t.set(' ')

    t.set(resultch)
    label_text.grid(row=3, column=0)



def down():
    global count
    count-=1
    if count<0:
        count=listlen-1
    print(path + '\\' + image_files[count])
    img = Image.open(path +'\\'+image_files[count])
    img = img.resize((576, 324), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img
    check_path = Path(image_files[count]).name
    with open(r'result.txt', 'r', encoding='utf8') as f:
        text = f.readlines()
    for i in range(len(text)):
        if check_path + '\n' == text[i]:
            print()
            resultch = text[i + 1]+'\n'+text[i + 2]+'\n'+text[i + 3]
    print(resultch)

    t.set(' ')

    t.set(resultch)
    label_text.grid(row=3, column=0)

root=tk.Tk()
root.title('相册')
path=r'F:\test'
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
btnup=Button(box,text="上一张", command=down)
btndown=Button(box,text="下一张", command=up)
btnup.grid(row=1, column=0)
btndown.grid(row=1, column=1)

t=tk.StringVar()
label_text=tk.Label(root,textvariable=t)

root.mainloop()
