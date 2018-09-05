from matplotlib import pyplot

from main_package.random.random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，就不断地模拟随机漫步
    rw = RandomWalk()
    rw.fill_walk()

    pint_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values, rw.y_values, c=pint_numbers, cmap=pyplot.cm.Reds, s=15)
    pyplot.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
