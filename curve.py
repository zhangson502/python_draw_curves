#coding=utf-8
#引入绘图工具
import matplotlib.pyplot as plt
import numpy as np
#支持汉语
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
# 构造数据
X=np.arange(-10,10,0.1)
Y=np.arange(-10,10,0.1)
Z=np.zeros((len(X),len(Y)),dtype=np.float32)
#开始绘制
fig = plt.figure('水滴下落模拟')
ax = fig.gca(projection='3d')
i=0.1   #临时变量，用于动图绘制

'''
    绘制动态图，一帧一帧的绘制
'''
while True:
    plt.cla()   #清空上一张动态图
    i += 0.2
    '''
            整理数据
        '''
    for y in range(len(Y)):
        for x in range(len(X)):
            tmp_1 = np.sqrt(X[x] * X[x] + Y[y] * Y[y])
            tmp = np.cos(tmp_1 - i) / (tmp_1 + i)
            Z[y][x] = tmp
    '''
            绘制网格
    '''
    XX, YY = np.meshgrid(X, Y)

    ax.set_title('物体落水波纹模拟')
    ax.set_zlim(-1, 1)  # 配置坐标系阈值
    ax.set_xlabel('X轴');
    ax.set_ylabel('Y轴');
    ax.set_zlabel('z轴')  # 配置轴标签

    surf = ax.plot_surface(XX, YY, Z, cmap='rainbow',antialiased=False)

    plt.pause(0.1)