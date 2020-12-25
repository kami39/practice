# -*- coding: gbk -*-
"""
Created on Sun Jan 11 11:51:41 2015

@author: zhang
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

data = np.random.randint(1, 5, (5, 2))
x = np.arange(len(data))

plt.plot(x, data[:, 0], '--', color = 'm')
plt.plot(x, data[:, 1], '-.', color = 'c')

plt.show()