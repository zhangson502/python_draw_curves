#coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
import numpy as np
import  numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

X=np.array([2005,2010,2015])
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
ax.set_xlabel('年份')
ax.set_ylabel('投入')
ax.set_zlabel('销售额')
ax.set_zlim(0,100)
ax.bar3d(X, Y, bottom, width, height, Z, shade=False,color='#fff')


plt.show()
