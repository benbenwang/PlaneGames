import time

from matplotlib import pyplot

from main_package.random.random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，就不断地模拟随机漫步
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口尺寸
    pyplot.figure(dpi=128, figsize=(10, 6))

    pint_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values, rw.y_values, c=pint_numbers, cmap=pyplot.cm.Reds, edgecolors='none', s=1)
    # 突出起点和终点
    pyplot.scatter(0, 0, c="green", edgecolors="none", s=100)
    pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)
    # 隐藏坐标轴
    pyplot.axes().get_xaxis().set_visible(False)
    pyplot.axes().get_yaxis().set_visible(False)
    pyplot.show()

    # keep_running = input("Make another walk? (y/n):")
    # if keep_running == 'n':
    #     break
    time.sleep(1)
