labels = ['男', '女','未知']  # 饼状图的标签
sizes = [52.74, 47.03, 0.23]  # 每个部分的占比

fig, ax = plt.subplots()

ax.set_title('性别分布')
ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼状图并添加标签和百分比显示

ax.legend()  # 添加图例

plt.show()
