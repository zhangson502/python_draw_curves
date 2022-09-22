#coding=utf-8
#引入绘图工具
import matplotlib.pyplot as plt
import numpy as np
#支持汉语
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

#开始绘制
fig = plt.figure('')
ax = fig.gca(projection='3d')

steps=30

pos=[0.010,0.000,0.16]
tar_1=[0.274,0.22,0.05]
tar_2=[0.274,0.22,0.0]
pList=[]

dx=(tar_1[0]-pos[0])/steps
dy=(tar_1[1]-pos[1])/steps
dz=(tar_1[2]-pos[2])/steps
for i in range(steps):
    pList.append([pos[0]+dx*i,pos[1]+dy*i,pos[2]+i*dz])
pList.append(tar_2)

pList=np.array(pList).transpose()

ax.set_xlabel('X(m)');ax.set_ylabel('Y(m)');ax.set_zlabel('Z(m)')
ax.set_xlim(0,0.3);ax.set_ylim(0,0.3);ax.set_zlim(0,0.2);

ax.plot(pList[0], pList[1], pList[2], '.-',color='g', label='动态范式/自主抓取')

pos=[0.010,0.000,0.16]
tar_1=[0.15,0.12,0.05]
tar_2=[0.15,0.12,0.0]
pList=[]

dx=(tar_1[0]-pos[0])/steps
dy=(tar_1[1]-pos[1])/steps
dz=(tar_1[2]-pos[2])/steps
for i in range(steps):
    pList.append([pos[0]+dx*i,pos[1]+dy*i,pos[2]+i*dz])
pList.append(tar_2)

pList=np.array(pList).transpose()
ax.plot(pList[0], pList[1], pList[2], '.-',color='g')

pos=[0.010,0.000,0.16]
tar_1=[0.2,0.25,0.05]
tar_2=[0.2,0.25,0.0]
pList=[]

dx=(tar_1[0]-pos[0])/steps
dy=(tar_1[1]-pos[1])/steps
dz=(tar_1[2]-pos[2])/steps
for i in range(steps):
    pList.append([pos[0]+dx*i,pos[1]+dy*i,pos[2]+i*dz])
pList.append(tar_2)

pList=np.array(pList).transpose()
ax.plot(pList[0], pList[1], pList[2], '.-',color='g')

pList=[[0.01,0.01,0.1],[0.01,0.04,0.1],[0.04,0.04,0.1],[0.06,0.04,0.1],[0.06,0.2,0.1],[0.18,0.2,0.1],[0.21,0.2,0.1],[0.21,0.24,0.1],[0.27,0.24,0.1],[0.27,0.21,0.1],[0.27,0.21,0.0]]
pList=np.array(pList).transpose()
ax.plot(pList[0], pList[1], pList[2], '--',color='r')


pList=[[0.01,0.01,0.1],[0.01,0.02,0.1],[0.04,0.02,0.1],[0.04,0.1,0.1],[0.1,0.1,0.1],[0.16,0.1,0.1],[0.16,0.2,0.1],[0.27,0.2,0.1],[0.2,0.2,0.1],[0.2,0.25,0.1],[0.2,0.25,0.0]]
pList=np.array(pList).transpose()
ax.plot(pList[0], pList[1], pList[2], '--',color='r')

pList=[[0.01,0.01,0.1],[0.05,0.01,0.1],[0.05,0.1,0.1],[0.07,0.1,0.1],[0.07,0.14,0.1],[0.1,0.14,0.1],[0.1,0.12,0.1],[0.15,0.12,0.1],[0.15,0.12,0.0]]
pList=np.array(pList).transpose()
ax.plot(pList[0], pList[1], pList[2], '--',color='r',label='静态范式/过程控制')
plt.legend()
plt.show()