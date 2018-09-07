from random import randint


class Die():
    """表示一个筛子的类"""

    def __init__(self, num_sides=6):
        """筛子默认6个面"""
        self.num_sizes = num_sides

    def roll(self):
        """返回一个位于1和筛子面数之间的随机数值"""
        return randint(1, self.num_sizes)

