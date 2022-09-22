#coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
import numpy as np
import  numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

X=np.array([10,20,30])
Y=np.array([0,20,40,60,80])
z=[[71.22620808,	31.62550135,	34.46955924,	35.50925463,	31.30233635],
[87.72249038,	56.62355997,	56.20567587,	43.36060399,	32.18126666],
[114.694559,		89.23325686,	78.57614746,	69.60779463,	44.54497901]]

Z=np.array(z).transpose()
X,Y=np.meshgrid(X,Y)
X, Y=X.ravel(), Y.ravel()
Z=Z.ravel()
bottom=np.zeros_like(X)
width=height=1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.bar3d(X, Y, bottom, width, height, Z, shade=False,color='b')

Z2=[[61.564853,	45.6259412,	35,	35,	35],
[74.8472795,		58.9083677,	42.9694559,	35,	35],
[114.694559,		98.7556472,	82.8167354,	66.8778236,	50.9389118]]

X2=X+1.2
Z2=np.array(Z2).transpose()
Z2=Z2.ravel()
ax.bar3d(X2, Y, bottom, width, height, Z2, shade=False,color='y',)

Z2=[[9.661355079,		14.00043985,	0.530440758,	0.509254631,	3.697663646],
[12.87521089,	2.284807731,	13.23621997,	8.360603989,	2.81873334],
[0,	0.53105489,4.240587938,	2.729971032,	6.393932786]
]
X2=X2+1.2
Z2=np.array(Z2).transpose()
Z2=Z2.ravel()
ax.bar3d(X2, Y, bottom, width, height, Z2, shade=False,color='r',label='误差')
plt.show()
