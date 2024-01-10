import tkinter as tk
from tkinter import ttk
#Tkinter与matplotlib交互，嵌入式图像
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import pandas as pd
# 设置中文字体
mpl.rcParams['font.family'] = 'SimHei'  # 楷体：SimKai，黑体：SimHei，微软雅黑：Microsoft YaHei

mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题


# 创建GUI窗口
window = tk.Tk()
window.title("公众号文章后台数据查询")
window.geometry("800x600")

#先隐藏窗口，登陆完再显示
window.withdraw()

# 创建一个外部的 框架
outer_frame = tk.Frame(window)
outer_frame.pack(side=tk.RIGHT)

# 创建文章数据显示区域
data_frame = ttk.Frame(window)
data_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)#fill填充

# 创建用户名和密码字典
user_dict = {"230207308": "20050807"}

# 创建登录窗口
login_window = tk.Toplevel(window)
login_frame = ttk.Frame(login_window)
login_frame.pack(padx=50, pady=50)
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_dict and user_dict[username] == password:
        #销毁登录窗口
        login_window.destroy()
        #显示主窗口
        window.deiconify()
    else:
        tk.messagebox.showerror("错误", "用户名或密码错误！")


login_button = ttk.Button(login_frame, text="登录", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 创建登录组件
username_label = ttk.Label(login_frame, text="用户名")
username_entry = ttk.Entry(login_frame)
password_label = ttk.Label(login_frame, text="密码")
password_entry = ttk.Entry(login_frame, show="*")

username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)




# 创建文章列表
def get_folder_names():
    folder_names = []
    #循环当前文件夹下的所有文件
    for folder in os.listdir('.'):
        #如果是文件类型是文件夹，并且不是.idea文件夹
        if os.path.isdir(folder) and folder != '.idea':
            #将他的名字加入folder_names
            folder_names.append(folder)
    #返回folder_names
    return folder_names


#获取所有文件夹，就是所有的文章
articles = get_folder_names()


#创建一个下拉列表
article_combobox = ttk.Combobox(data_frame, values=articles,state='readonly')
article_combobox.grid(row=0, column=0, padx=10, pady=10)


#获取下拉列表的数据以判断是哪篇文章
def get_selected_data():
    selected_value = article_combobox.get()
    return selected_value

# 阅读人数和次数
def show_data1():

    selected_data = get_selected_data()
    if not selected_data:
        return
    #读取csv数据
    data = pd.read_csv(fr'{selected_data}\\1.csv')
    x = list(set(data['日期']))  # x轴数据,去重
    x.sort()
    grouped = data[data['传播渠道'] =='全部']#根据条件返回bool序列，筛选出每天的全部行

    #用于重置索引并丢弃原来的索引列
    y1 = grouped['阅读人数'].reset_index(drop=True)
    y2 = grouped['阅读次数'].reset_index(drop=True)

    # 创建画布
    fig = canvas.figure
    fig.clear()
    #创建子图，更灵活
    ax = fig.add_subplot()

    # 给图像命名
    ax.set_title('阅读人数和阅读次数')

    ax.plot(x, y1, label='阅读人数')
    ax.plot(x, y2, label='阅读次数')

    # 标识每个点的数值
    for i in range(len(x)):
        ax.annotate(str(y1[i]), (x[i], y1[i]), textcoords="offset points", xytext=(0, -15), ha='center')
        ax.annotate(str(y2[i]), (x[i], y2[i]), textcoords="offset points", xytext=(0, 10), ha='center')
        ax.scatter(x[i], y1[i], marker='D', color='red')
        ax.scatter(x[i], y2[i], marker='D', color='blue')

    # 图例
    ax.legend(['阅读人数', '阅读次数'])

    ax.set_xlabel('日期')
    ax.set_ylabel('次数')

    canvas.draw()

    pass

# 阅读完成情况
def show_data2():
    selected_data = get_selected_data()
    if not selected_data:
        return
    data = pd.read_csv(fr'{selected_data}\\2.csv')

    #处理百分数数据的函数
    def format_func(s):
        s=float(s.strip('%'))
        return s
    #对每个元素分别处理
    x = list(map(format_func,data['浏览位置']))  # x轴数据
    y = list(map(format_func,data['跳出比例'])) # y轴数据

    fig = canvas.figure
    fig.clear()
    ax = fig.add_subplot()

    ax.set_title('阅读完成情况')
    ax.bar(x, y, color='green')

    ax.set_xlabel('浏览位置/%')
    ax.set_ylabel('跳出比例/%')

    canvas.draw()



# 性别分布
def show_data3():
    selected_data = get_selected_data()
    if not selected_data:
        return
    data = pd.read_csv(fr'{selected_data}\\3.csv')

    labels = data['性别'] # 饼状图的标签
    sizes = [s.strip('%') for s in data['占比']] # 每个部分的占比

    fig = canvas.figure
    fig.clear()
    ax = fig.add_subplot()

    ax.set_title('性别分布')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼状图并添加标签和百分比显示

    ax.legend()  # 添加图例

    canvas.draw()
    pass

# 性别分布
def show_data4():
    selected_data = get_selected_data()
    if not selected_data:
        return
    data = pd.read_csv(fr'{selected_data}\\4.csv')

    labels = data['年龄']  # 饼状图的标签
    sizes = [s.strip('%') for s in data['占比']]  # 每个部分的占比

    fig = canvas.figure
    fig.clear()
    ax = fig.add_subplot()

    ax.set_title('性别分布')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼状图并添加标签和百分比显示

    ax.legend(loc='upper left')  # 添加图例，并将其位置设置为最右下角

    canvas.draw()
    pass
def show_data5():
    selected_data = get_selected_data()
    if not selected_data:
        return
    data = pd.read_csv(fr'{selected_data}\\5.csv')

    # 提取省份/直辖市名称和人数
    provinces = data['省份/直辖市']
    counts = data['人数']

    # 创建Matplotlib图形区域和子图
    fig = canvas.figure
    fig.clear()
    ax = fig.add_subplot()

    # 绘制柱状图
    bars = ax.bar(range(len(provinces)), counts)
    ax.set_xticks(range(len(provinces)))
    ax.set_xticklabels(provinces, rotation=90)
    ax.set_xlabel('省份/直辖市')
    ax.set_ylabel('人数')
    ax.set_title('中国各省份/直辖市人数分布')
    ax.bar_label(bars, fmt='%d')

    # 将图像绘制到canvas中
    canvas.draw()
    pass


def flower():
    # 一朵花
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator
    import matplotlib.pyplot as plt
    import numpy as np

    fig = canvas.figure
    fig.clear()
    ax = fig.add_subplot(111, projection='3d')  # 使用 add_subplot() 创建三维坐标轴

    [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))

    surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p)), rstride=1, cstride=1,
                           cmap=cm.Reds_r, linewidth=0, antialiased=True)

    plt.title('Love Rose')
    canvas.draw()




# 创建按钮并添加到外部 Frame
button1 = tk.Button(outer_frame, text="浏览人数与浏览次数", command=show_data1)
button2 = tk.Button(outer_frame, text="阅读完成情况", command=show_data2)
button3 = tk.Button(outer_frame, text="性别分布", command=show_data3)
button4 = tk.Button(outer_frame, text="年龄分布", command=show_data4)
button5 = tk.Button(outer_frame, text="地域分布", command=show_data5)
button6 = tk.Button(outer_frame, text="flower", command=flower)

# 设置按钮整体位置
button1.pack(side=tk.TOP)
button2.pack(side=tk.TOP)
button3.pack(side=tk.TOP)
button4.pack(side=tk.TOP)
button5.pack(side=tk.TOP)
button6.pack(side=tk.TOP)

# 创建Matplotlib图形区域
fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# 运行GUI程序
window.mainloop()












