# 封装一个滑动方法

class Swipe:
    # def __init__(self):
    # pass
    def swipeUp(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # 起始x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['heigth'] * 0.25  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # 起始x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.75  # 起始x坐标
        y1 = l['height'] * 0.5  # 起始y坐标
        x2 = l['width'] * 0.05  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)

    def swipeRigth(driver, t=500, n=1):
        l = driver.get_window_size()
        x1 = l['width'] * 0.05  # 起始x坐标
        y1 = l['height'] * 0.5  # 起始y坐标
        x2 = l['width'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x2, y1, t)
        if __name__ == "__main__":
            print(driver.get_window_size())
