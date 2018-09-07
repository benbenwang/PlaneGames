from matplotlib import pyplot

# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]
# pyplot.scatter(x_value, y_value, c="red", edgecolors="none", s=40)
# pyplot.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors="none", s=40)
pyplot.scatter(x_value, y_value, c=y_value, cmap=pyplot.cm.Reds, edgecolors="none", s=40)
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
pyplot.tick_params(axis="both", which="major", labelsize=14)

# 设置每个坐标轴的取值范围
pyplot.axis([0, 1100, 0, 1100000])
pyplot.show()
# 保存图表
pyplot.savefig('D:\squares_plot.png', bbox_inches="tight")
