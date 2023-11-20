import tkinter as tk
def show_content():
    content = '00：00 人在海滩上\n00：05 人在走 \n00: 09 许多人在走'# 获取文本框中的内容
    label.config(text=content)  # 将内容输出到标签中
# 创建窗口和控件
root = tk.Tk()
root.geometry('1000x200')
btn = tk.Button(root, text='显示内容', command=show_content)  # 创建按钮
label = tk.Label(root)  # 创建标签
# 将控件添加到窗口中
btn.pack(pady=10)
label.pack()
root.mainloop()  # 进入事件循环