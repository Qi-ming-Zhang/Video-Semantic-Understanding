import tkinter as tk
import vlc


class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # 创建GUI界面
        self.create_widgets()

    def create_widgets(self):
        # 创建Canvas用于播放视频
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        # 添加按钮控制视频播放
        self.play_button = tk.Button(self.master, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        # 添加滑动条控制音量 a group of people are standing on a beach
        # a group of people are standing on a beach
        # a group of people are standing on a bed
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack(side=tk.BOTTOM)

        # 加载视频文件
        self.media = self.instance.media_new(
            'D://student/testvideo.mp4')
        self.player.set_media(self.media)



    def play(self):
        # 开始播放视频
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


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video Player")
    player = VideoPlayer(root)
    root.mainloop()