#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
문제: 확률을 이용하여 PI 값을 근사하는 프로그램.
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 2.5))   # plot을 나타낼 Figure 객체 생성
plt.ylabel('in_y and out_y')
for column in range(3):
    subplot = fig.add_subplot(1, 3, column+1)   # (X, Y, Z): X x Y (행x열)의 Z번째
    subplot.set_xlim([0, 1])    # 해당 plot의 x축의 범위를 제한 [0, 1)
    subplot.set_ylim([0, 1])    # 해당 plot의 y축의 범위를 제한 [0, 1)

    circle = plt.Circle((0, 0), radius=1, color='black', fill=False)
    subplot.add_artist(circle)
    
    in_x, in_y = [], []
    out_x, out_y = [], []
    steps = 10 * pow(10, column+1)
    matches = 0
    plt.xlabel('in_x and out_x')
    for _ in range(steps):
        x=np.random.rand()
        y=np.random.rand()
        
        isin = (x*x + y*y) <= 1
        matches += isin
        if isin:
            in_x.append(x)
            in_y.append(y)
        else:
            out_x.append(x)
            out_y.append(y)

    PI = matches / steps * 4

    
    plt.scatter(in_x, in_y, c="blue", s=0.1)
    plt.scatter(out_x, out_y, c="red", s=0.1)

    plt.title("steps: " + str(steps))
    print('[steps] %d' % steps)
    print('mathces: %d / %d' % (matches, steps))
    print('pi: %.10f' % np.pi)
    
    print('approximate pi: %.10f' % PI)
    print('difference: %.10f\n' % (abs(np.pi - PI)))


plt.legend(['in_x,in_y', 'out_x,out_y'],bbox_to_anchor=(1, 1)) 

plt.show()
