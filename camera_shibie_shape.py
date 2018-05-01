#coding=utf-8
from pyfirmata import Arduino, util
import time
import cv2
import  numpy as np
import serial
ser = serial.Serial()
ser.baudrate = 9600  # 设置波特率
ser.port = 'COM6'  # 端口是COM3
print(ser)
ser.open()  # 打开串口
print(ser.is_open)  # 检验串口是否打开
# board = Arduino('COM3')
"""
def duoji ():
    board.servo_config(13, 0, 255, 20)
    print("ceshi")
    time.sleep(0.2)
    board.servo_config(13, 0, 255, 255)
    time.sleep(0.2)
def arduino ():
    board.digital[13].write(0)  # 向io口13写入0
    time.sleep(0.1)
    board.digital[13].write(1)  # 向io口13写入1
    time.sleep(0.1)
    board.analog [13].write(100)
"""
def detect_circle_demo ():
    video_capture = cv2.VideoCapture(0)
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            break
        ret, img = video_capture.read()
        #img = cv2.pyrMeanShiftFiltering(img, 10, 25)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
        circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT , 1, 100, param1=100, param2=100, minRadius=50,maxRadius=200)
       # cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        try:  # 如果上一步没有检测到。执行try内容，就会报错。可以修改尝试看下。
            circles = circles1[0, :, :]  # 提取为二维
        except TypeError:
            print('未发现圆形物体！！')
        else:
            circles = np.uint16(np.around(circles))  # 四舍五入
            for i in circles[:]:
                cv2.circle(img, (i[0], i[1]), i[2], color=[0, 0, 0], thickness=2)  # 画圆
                cv2.circle(img, (i[0], i[1]), 2, color=[0, 255, 0], thickness=2)  # 画圆心
                cv2.putText(img, "center", (i[0] - 20, i[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                print(i[0],i[1])
                print("检测到圆形物体，开始分离！")
                ser.write(b"a")
                #print(ser.read(1))
                # 输出坐标
        # 显示视频
        cv2.imshow('Video', img)
        cv2.waitKey(10)
detect_circle_demo()


"""
dp，用来检测圆心的累加器图像的分辨率于输入图像之比的倒数，且此参数允许创建一个比输入图像分辨率低的累加器。上述文字不好理解的话，来看例子吧。例如，如果dp= 1时，累加器和输入图像具有相同的分辨率。如果dp=2，累加器便有输入图像一半那么大的宽度和高度。
minDist，为霍夫变换检测到的圆的圆心之间的最小距离，即让我们的算法能明显区分的两个不同圆之间的最小距离。这个参数如果太小的话，多个相邻的圆可能被错误地检测成了一个重合的圆。反之，这个参数设置太大的话，某些圆就不能被检测出来了。
param1，有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半。
param2，也有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示在检测阶段圆心的累加器阈值。它越小的话，就可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了。
minRadius，默认值0，表示圆半径的最小值。
maxRadius，也有默认值0，表示圆半径的最大值
"""