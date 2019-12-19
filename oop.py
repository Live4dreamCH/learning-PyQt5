from math import sqrt


class Point:
    """这是个平面点类，有两个坐标：x和y"""

    count = 0
    "有几个点"

    def __init__(self, x=0, y=0):
        """新建点，并默认初始化x，y为0,0"""
        self.x = x
        self.y = y
        Point.count += 1

    def move(self, x, y):
        """移动点坐标"""
        self.x = x
        self.y = y

    def reset(self):
        """重置点坐标到原点，为0,0"""
        self.move(0, 0)

    def dis(self, point2):
        """计算两点间距离"""
        return sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)

    def print(self):
        print(Point.count)
        print((self.x, self.y))


if __name__ == '__main__':
    a = Point(y=1, x=2)
    b = Point()
    assert (a.dis(b) == b.dis(a))
    a.print()
    b.print()
    print(a.dis(b))
