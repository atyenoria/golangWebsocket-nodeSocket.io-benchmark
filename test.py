import csv
import pandas as pd
import pandas.io.data as web
from matplotlib import pylab as pl
from scipy.stats import norm
from numpy.random import *
import numpy as np
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines as mlines

csv = np.genfromtxt ('./3000_output.csv', delimiter=",")
second = csv[:,2]
third = csv[:,6]
x=second[0:10]


y1=third[0:10]
c1="Concurrency="+str(second[1])
y2=third[11:21]
c2="Concurrency="+str(second[11])

y3=third[21:31]
c3="Concurrency="+str(second[21])

a1 = mlines.Line2D([], [], color='blue', marker='*',
                          markersize=15, label=c1)
a2 = mlines.Line2D([], [], color='red', marker='*',
                          markersize=15, label='Blue stars')
a3 = mlines.Line2D([], [], color='green', marker='*',
                          markersize=15, label='Blue stars')
a4 = mlines.Line2D([], [], color='yellow', marker='*',
                          markersize=15, label='Blue stars')

# pl.plot(x, y2, marker='o', label='Line 1')

# pl.legend(handles=[a1,a2])
line1, = pl.plot(x,y1 ,marker='o', label=c1)
line2, = pl.plot(x,y2 ,marker='o', label=c2)
line2, = pl.plot(x,y3 ,marker='o', label=c3)

pl.legend(handler_map={line1: HandlerLine2D(numpoints=4)})




pl.xlim([0, 1000])
pl.ylim([0, 100000])
pl.title("Node.js Socket.io Performance", fontsize = 20)
pl.xlabel("Total Connections (times)")
pl.ylabel("Round Trip Duration Time (ms)")
pl.savefig("graph1.png")
pl.show()

