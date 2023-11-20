import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import vlc
import cv2


class VideoPlayer:
    def __init__(self, master):

        self.master = master
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        # 创建GUI界面
        self.create_widgets()



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

        # 打开文件夹按钮
        self.open_folder_button = tk.Button(self.master, text="打开文件夹", command=self.open_folder, width=10,height=4)
        self.open_folder_button.pack(side=tk.TOP)

        # 列表框
        self.listbox = tk.Listbox(self.master, width=100, height=20)
        s = ttk.Scrollbar(root, orient=VERTICAL, command=self.listbox.yview)
        #s.pack(side=tk.RIGHT, fill=tk.Y, anchor=E)
        self.listbox.config(yscrollcommand=s.set)
        self.listbox.pack()



        # 添加滑动条控制音量 a group of people are standing on a beach
        # a group of people are standing on a beach
        # a group of people are standing on a bed
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack(side=tk.BOTTOM)

        # 加载视频文件


    def play(self):
        # 开始播放视频
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_path = self.listbox.get(selected_index)
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
        video_extensions = ['.mp4', '.mkv', '.avi', '.mov']
        file_path_list = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if os.path.splitext(file)[1] in video_extensions:
                    file_path_list.append(os.path.join(root, file))
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

