from matplotlib import pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
pyplot.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
pyplot.title("Square Number", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)
# 设置刻度标记大小
pyplot.tick_params(axis='both', labelsize=14)
pyplot.show()
