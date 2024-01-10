labels = ['60岁以上','46-60岁','36-45岁', '26-35岁','18-25岁','18岁以下']  # 饼状图的标签
sizes = [4.49, 31.1, 37.27,22,4.64,0.5]  # 每个部分的占比

fig, ax = plt.subplots()

ax.set_title('性别分布')
ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼状图并添加标签和百分比显示

ax.legend(loc='upper left')  # 添加图例，并将其位置设置为最右下角

plt.show()