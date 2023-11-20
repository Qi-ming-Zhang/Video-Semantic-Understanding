import os
import random
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import vlc
import cv2
import ui_4
import ui_5
from PIL import Image,ImageTk
from tqdm.tk import tqdm
from tkinter import messagebox
import threading

class VideoPlayer:
    def __init__(self, master):

        self.master = master
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        # 创建GUI界面
        self.create_widgets()
        self.predict_path=""
        self.save=r"F:\test"   #保存图片路径
        self.count=1



    def create_widgets(self):
        # 创建Canvas用于播放视频
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack()

        # 添加按钮控制视频播放
        self.play_button = tk.Button(self.master, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.master, text="predict", command=self.predict)
        self.stop_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.master, text="result", command=self.result)
        self.stop_button.pack(side=tk.LEFT)

        # 打开文件夹按钮
        self.open_folder_button = tk.Button(self.master, text="打开文件夹", command=self.open_folder, width=10,height=4)
        self.open_folder_button.pack(side=tk.TOP)

        # 列表框
        self.listbox = tk.Listbox(self.master, width=100, height=20)
        s = ttk.Scrollbar(root, orient=VERTICAL, command=self.listbox.yview)
        #s.pack(side=tk.RIGHT, fill=tk.Y, anchor=E)
        self.listbox.config(yscrollcommand=s.set)
        self.listbox.pack()



        # 添加滑动条控制音量
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack(side=tk.BOTTOM)

        # 加载视频文件

    def result(self):
        top = tk.Toplevel()
        # count = 1

        def get_image_files(directory):
            image_files = []
            for file in os.listdir(directory):
                if file.endswith(".png"):
                    image_files.append(file)
            return image_files

        def up():
            # global count
            self.count += 1
            if self.count > listlen - 1:
                self.count = 0
            print(path + '\\' + image_files[self.count])
            img = Image.open(path + '\\' + image_files[self.count])
            img = img.resize((576, 324), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img
            check_path = Path(image_files[self.count]).name
            with open(r'result.txt', 'r', encoding='utf8') as f:
                text = f.readlines()
            for i in range(len(text)):
                if check_path + '\n' == text[i]:
                    print()
                    resultch = text[i + 1] + '\n' + text[i + 2] + '\n' + text[i + 3]
            print(resultch)

            t.set(' ')

            t.set(resultch)
            label_text.grid(row=3, column=0)

        def down():

            self.count -= 1
            if self.count < 0:
                self.count = listlen - 1
            print(path + '\\' + image_files[self.count])
            img = Image.open(path + '\\' + image_files[self.count])
            img = img.resize((576, 324), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img
            check_path = Path(image_files[self.count]).name
            with open(r'result.txt', 'r', encoding='utf8') as f:
                text = f.readlines()
            for i in range(len(text)):
                if check_path + '\n' == text[i]:
                    print()
                    resultch = text[i + 1] + '\n' + text[i + 2] + '\n' + text[i + 3]
            print(resultch)

            t.set(' ')

            t.set(resultch)
            label_text.grid(row=3, column=0)


        top.title('相册')
        path = r'F:\test'
        image_files = get_image_files(path)
        print(image_files[0])
        listlen: int = len(image_files)
        print(listlen)
        tk.Label(top, width=40, height=3, wraplength=80)
        img = Image.open(path + '\\' + image_files[0])
        img = img.resize((576, 324), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        box = Frame(top, width=600, height=400, borderwidth=5)
        box.grid(row=0, column=0)
        label = Label(box, width=600, height=337, image=img)
        label.grid(row=0, columnspan=2)
        btnup = Button(box, text="上一张", command=down)
        btndown = Button(box, text="下一张", command=up)
        btnup.grid(row=1, column=0)
        btndown.grid(row=1, column=1)

        t = tk.StringVar()
        label_text = tk.Label(top, textvariable=t)

        # root.mainloop()


    def predict(self):
        def thread_predict():

            # self.predict_path
            ui_4.vidio_frame_extract(self.predict_path,self.save,1000)
            filelist = os.listdir(self.save)

            #file = filedialog.askopenfilename(filetypes=(("img files", "*.png"), ("img1 files", "*.jpg"), ("all files", "*.*")))
            #trs_list=ui_4.predict(file)
            #file是选取的图像
            samplelist = random.sample(filelist, 1)  # 调整  随机取一张图片
            print(samplelist)
            for imgpath in tqdm(filelist,total=len(filelist), tk_parent=root):
                print(imgpath)
                imgrealpath = os.path.join(self.save, imgpath)
                im = Image.open(imgrealpath)
                #im.show()
                trs_list=ui_4.predict(imgrealpath)
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(imgpath)
                    # f.write(" ")
                    f.write(("\n"))
                    for i in trs_list:
                        f.write(i)
                        f.write(("\n"))
                    f.close()

            messagebox.showinfo(message='预测完成')
        threading.Thread(target=thread_predict).start()
        # top=tk.Toplevel()
        # print(imgrealpath)
        # #img_open=Image.open(file)
        # img_open = Image.open(imgrealpath)
        # # img = ImageTk.PhotoImage(img_open.resize((200,200)))
        # global img
        # img_open=img_open.resize((576,324),Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(img_open)
        #
        # img_cav=tk.Canvas(top)
        # img_cav.create_image(0,0,image=img)
        # img_cav.pack()
        # for i in trs_list:
        #     tk.Label(top,text=i).pack()
        # pass

    def play(self):
        # 开始播放视频
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_path = self.listbox.get(selected_index)
            # print(selected_path)
            self.predict_path=selected_path
            self.media = self.instance.media_new(selected_path)
            self.player.set_media(self.media)
        self.player.play()

    def pause(self):
        # 暂停播放视频
        self.player.pause()

    def stop(self):
        # 停止播放视频
        self.player.stop()

    def set_volume(self, volume):
        # 设置音量
        self.player.audio_set_volume(int(volume))

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_path_list = self.find_videos(folder_path)
            self.update_listbox()

    def find_videos(self, folder_path):
        video_extensions = ['.mp4', '.mkv', '.avi', '.mov','.MP4']
        file_path_list = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if os.path.splitext(file)[1] in video_extensions:
                    file_path_list.append(os.path.join(root, file))
                    # print(file_path_list)
        return file_path_list

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file_path in self.file_path_list:
            self.listbox.insert(tk.END, file_path)






if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video Player")
    player = VideoPlayer(root)
    root.mainloop()

