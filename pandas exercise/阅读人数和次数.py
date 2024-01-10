x = [1214, 1215, 1216, 1217, 1218, 1219, 1220]  # x轴数据
y1 = [14589, 7983, 75, 24, 15, 6, 6]  # 第一条曲线的y轴数据
y2 = [16357, 8818, 77, 24, 19, 6, 6]  # 第二条曲线的y轴数据

#创建画布
fig, ax = plt.subplots()

#给图像命名
ax.set_title('阅读人数和阅读次数')

ax.plot(x, y1, label='阅读人数')
ax.plot(x, y2, label='阅读次数')

# 标识每个点的数值
for i in range(len(x)):
    ax.annotate(str(y1[i]), (x[i], y1[i]), textcoords="offset points", xytext=(0, -15), ha='center')
    ax.annotate(str(y2[i]), (x[i], y2[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    ax.scatter(x[i], y1[i], marker='D', color='red')
    ax.scatter(x[i], y2[i], marker='D', color='blue')

#图例
ax.legend(['阅读人数', '阅读次数'])

ax.set_xlabel('日期')
ax.set_ylabel('次数')

plt.show()