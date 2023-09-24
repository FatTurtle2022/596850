# 导入subprocess和os模块，它们可以让你在Python中执行外部命令和操作文件系统
import subprocess
import os
import tkinter as tk
import tkinter.filedialog as fd

video = 'error'
second= 3.08
files_name = ['error', 'error']
head_or_tail = 'tail'
second_time = 'auto'

window = tk.Tk()
window.title('肥胖龟自动去除片尾')
window.geometry('500x240')

title = tk.Label(window, text='肥胖龟自动去除片尾', bg='white', font=('Arial,12'), width=51, height=2)
title.place(x=0,y=0)

# 定义一个函数，用于调用文件选择对话框并获取文件名
def select_file():
    global files_name
    # 弹出文件选择对话框，并将返回值赋给files变量
    files = fd.askopenfilenames()
    # 如果用户选择了至少一个文件，而不是取消或关闭对话框
    if files:
        # 清空files_name列表，以便重新存储用户选择的文件名
        files_name.clear()
        # 遍历files列表中的每个文件名
        for file_name in files:
            # 对每个文件进行处理，例如打印文件名
            print(file_name)
            # 将文件名添加到files_name列表中
            files_name.append(file_name)

# 创建一个按钮，点击后弹出文件选择对话框
choose = tk.Button(window, text="选择文件", width=10, height=2, command=lambda: select_file())
choose.place(x='420',y='0')

var2 = tk.StringVar()
var3 = tk.StringVar()

var2.set('tail')
head_or_tail = 'tail'

second_Entry = tk.Entry(window,show=None)
second_Entry.place(x=0,y=90,width=415,height=40)

def set_second():
    global second
    global second_time
    if var3.get == 'zidingyi':
        second_time = 'zidingyi'
    if second_time == 'zidingyi':
        second = second_Entry.get()
    print(second)

set_second_Button = tk.Button(window, text="确定秒数", width=10, height=2, command=set_second)
set_second_Button.place(x=420,y=90)

def xiaohongshu():
    global second
    global second_time
    second = 3.08
    second_time = 'auto'

xiaohongshu_Button = tk.Radiobutton(window, text="自动去除小红书片尾",variable=var3,value='xiaohongshu',command=xiaohongshu)
xiaohongshu_Button.place(x=0,y=140)

def kuaishou():
    global second
    global second_time
    second = 3.64
    second_time = 'auto'

kuaishou_Button = tk.Radiobutton(window, text="自动去除快手片尾",variable=var3,value='kuaishou',command=kuaishou)
kuaishou_Button.place(x=140,y=140)

def douyin():
    global second
    global second_time
    second = 3.07
    second_time = 'auto'

douyin_Button = tk.Radiobutton(window, text="自动去除抖音片尾",variable=var3,value='douyin',command=xiaohongshu)
douyin_Button.place(x=280,y=140)

def zidingyi():
    global second
    global second_time
    second_time = 'zidingyi'
    second = second_Entry.get()
    print(second)

zidingyi_Button = tk.Radiobutton(window, text="自定义",variable=var3,value='zidingyi',command=zidingyi)
zidingyi_Button.place(x=420,y=140)

var3.set('xiaohongshu')

def change_head():
    global head_or_tail
    global second_time
    head_or_tail = 'head'
    xiaohongshu_Button.place_forget()
    douyin_Button.place_forget()
    kuaishou_Button.place_forget()
    var3.set('zidingyi')
    second_time = 'zidingyi'

head = tk.Radiobutton(window,text='自动去除片头',command=change_head,variable=var2,value='head')
head.place(x=0,y=45)

def change_tail():
    global head_or_tail
    head_or_tail = 'tail'
    xiaohongshu_Button.place(x=0,y=140)
    kuaishou_Button.place(x=140,y=140)
    douyin_Button.place(x=280,y=140)

tail = tk.Radiobutton(window,text='自动去除片尾',command=change_tail,variable=var2,value='tail')
tail.place(x=100,y=45)

def cut(video):
    global head_or_tail
    global second
    print(second)
    print(head_or_tail)
    if head_or_tail == 'tail':
        print(video)
        # 使用ffprobe命令获取视频的持续时间（以秒为单位），并将其转换为浮点数
        duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video]))

        # 计算要裁剪的视频片段的开始时间和结束时间
        start = 0
        end = duration - float(second)

        print(start)
        print(end)

        # 生成新的输出文件名，它与原视频文件名相同，但是在后缀前加了'_trimmed'
        output = os.path.join(os.path.dirname(video), os.path.basename(video).split('.')[0] + '_trimmed.' + os.path.basename(video).split('.')[1])

        # 执行ffmpeg命令来裁剪视频，使用'-ss'和'-to'参数指定开始时间和结束时间，使用'-c copy'参数保持原始的编码格式，使用'-movflags faststart'参数优化输出文件的格式
        subprocess.call(['ffmpeg', '-y', '-ss' , str(start), '-to', str(end), '-i', video,'-c', 'copy', output])
    if head_or_tail == 'head':
        print(video)
        # 使用ffprobe命令获取视频的持续时间（以秒为单位），并将其转换为浮点数
        duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video]))

        # 计算要裁剪的视频片段的开始时间和结束时间
        start = second
        end = duration

        print(start)
        print(end)

        # 生成新的输出文件名，它与原视频文件名相同，但是在后缀前加了'_trimmed'
        output = os.path.join(os.path.dirname(video), os.path.basename(video).split('.')[0] + '_trimmed.' + os.path.basename(video).split('.')[1])

        # 执行ffmpeg命令来裁剪视频，使用'-ss'和'-to'参数指定开始时间和结束时间，使用'-c copy'参数保持原始的编码格式，使用'-movflags faststart'参数优化输出文件的格式
        subprocess.call(['ffmpeg', '-ss', str(start), '-to', str(end), '-i', video, '-c:v', 'copy', output])
        #ffmpeg -ss 15 -to 98 -i input.mp4 -c:v copy output.mp4

def cut2():
    global files_name # 声明使用全局变量files_name
    global video
    # 遍历files_name列表中的每个文件名
    for file_name in files_name:
        # 调用cut函数来裁剪视频，传入文件名作为参数
        video = file_name
        cut(file_name)


cut_Button = tk.Button(window, text="剪辑，启动！", width=34, height=2, command=cut2)
cut_Button.place(x=0,y=190)

def about():
    about_window = tk.Toplevel()
    about_window.title('肥胖龟自动去除片尾 - 关于软件')
    about_window.geometry('800x125')

    about_text = tk.Label(about_window, text='肥胖龟自动去除片尾：是一款由肥胖龟（隶属于肥胖龟公司、TL工作室）开发的自动去除片尾软件。', bg='white', font=('Arial', 12))
    about_text.pack()

    about_text_2 = tk.Label(about_window, text='联系作者：QQ2947158920，邮箱qianzhemayi1234567@163.com，哔哩哔哩肥胖龟。', bg='white', font=('Arial', 12))
    about_text_2.pack()

    about_text_3 = tk.Label(about_window, text='Copyright © FATTURTLE INC. & TL Studio 2023；版权所有：肥胖龟公司及TL工作室。', bg='white', font=('Arial', 12))
    about_text_3.pack()

    def juanxian():
        os.system('start https://postimg.cc/K121LGX9')

    juanxian_Button = tk.Button(about_window,text='捐献', width=55, height=2, command=juanxian)
    juanxian_Button.place(x=0, y=75)

    def kaiyuan():
        os.system('start https://github.com/FatTurtle2022/FatTurtle_Cut_End/releases')

    kaiyuan_Button = tk.Button(about_window,text='开源', width=55, height=2, command=kaiyuan)
    kaiyuan_Button.place(x=400, y=75)

    about_window.mainloop()

about_Button = tk.Button(window,text='关于我们', width=34, height=2, command=about)
about_Button.place(x=250, y=190)

# 启动窗口的主循环
window.mainloop()