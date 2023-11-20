import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import vlc
import cv2

global selected_index
class VideoPlayer:
    def __init__(self):
        self.instance = vlc.Instance('--no-xlib')
        self.player = self.instance.media_player_new()

    def play(self, file_path):
        media = self.instance.media_new(file_path)
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    # 恢复
    def resume(self):
        self.player.set_pause(0)

    # 停止
    def stop(self):
        self.player.stop()






class App:
    def __init__(self, master):
        self.master = master
        self.master.title("视频播放器")
        self.file_path_list = []

        # 打开文件夹按钮
        self.open_folder_button = tk.Button(self.master, text="打开文件夹", command=self.open_folder,width=10,height=4)
        self.open_folder_button.pack()

        # 列表框
        self.listbox = tk.Listbox(self.master,width=100,height=20)
        s=ttk.Scrollbar(root,orient=VERTICAL,command=self.listbox.yview)
        s.pack(side=tk.RIGHT,fill=tk.Y,anchor=E)
        self.listbox.config(yscrollcommand=s.set)
        self.listbox.pack()

        # 播放按钮
        self.play_button = tk.Button(self.master, text="播放", command=self.play_video,width=10,height=4)
        self.play_button.pack(side=tk.LEFT)

        self.btn = tk.Button(self.master, text='显示内容', command=self.show_content,width=10,height=4)  # 创建按钮
        self.btn.pack(side=tk.LEFT)






    def show_content(self):
        content = 'a group of people are standing on a beach \
        a group of people are standing on a beach \
        a group of people are standing on a bed'
        label.config(text=content)  # 将内容输出到标签中

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

    def play_video(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_path = self.listbox.get(selected_index)
            player = VideoPlayer()
            player.play(selected_path)

class video_cv:
    def vidio_frame_extract(video_path,save_path,index):
        capture = cv2.VideoCapture(video_path)
        while capture.isOpened():
            ret, frame = capture.read()  # frame是BGR格式
            if not ret:
                print('loss this frame')
            if frame is None:
                break
            print(frame.shape)  # (795, 1055, 3)
            cv2.imshow('frame', frame)
            save_frame = "{}/{:>03d}.bmp".format(save_path, index)
            cv2.imwrite(save_frame, frame)
            index = index + 1
        capture.release()
        cv2.destroyAllWindows()

    def totalnumber_of_videoframes(video_path):
        capture = cv2.VideoCapture(video_path)
        len_video_frame = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        print('total number of video frames :', len_video_frame)
        n = 0
        loss_frames = []
        for i in range(len_video_frame):
            ret, frame = capture.read()  # ret返回的是True或者False，代表有没有读取到图像
            if ret:
                n += 1
            else:
                print("loss this frame")
                loss_frames.append(i)
        print('index :{}, read: {}'.format(i, n))
        print(loss_frames)











root = tk.Tk()
root.geometry('800x600')
label = tk.Label(root)
app = App(root)

save_path = "D:\oedio11"
index=0
video_cv.totalnumber_of_videoframes(selected_index)#先看一下视频本身实际有多少帧，再看真正保存的视频帧有多少
video_cv.vidio_frame_extract(selected_index, save_path, index)

root.mainloop()
