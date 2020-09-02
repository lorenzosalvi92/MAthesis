# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:51:48 2019

@author: Lorenzo
"""
import numpy as np
from matplotlib import pyplot as plt
from pylab import rcParams
from collections import Counter


'''                                                                
Bet:
a) status quo (100\$)
b) 50/50 chance of gain or loss, with gain of 50% and loss of 40%.
    
The Kelly criterion tells us that the optimal share of wealth to bet is 25\%.
'''

# creating array with 6 different percentages of wealth to bet (the third is the optimal share)
bet_size = np.asarray([0.1, 0.15, 0.25, 0.50, 0.6])
s = bet_size.size

# setting random seed
np.random.seed(2)

# coin flips: if 1, +50\% of wager; if 0, -40\% of wager
coinflips = np.random.randint(0, 2, 10001)
# counting the coinflips
counter = Counter(coinflips)

# creating storage matrix for six trajectories over 10000 time steps
data = np.zeros((5,10001))

# creating the trajectories
for j in range(0,5):
    print(bet_size[j,])
    X_0 = 100
    # starting capital
    for i in range(1,10001):
       if coinflips[i,] == 1: X_0 = X_0*(1+(bet_size[j,]*0.5))
       else: X_0 = X_0*(1-(bet_size[j,]*0.4))
       #print(w)
       data[j,i] = X_0

# 100 $ as a starting value for all the trajectories
data[:,0] = 100

# plotting the trajectories
# the optimal share trajectory is the magenta, dashed line
rcParams['figure.figsize'] = 12, 5
plt.gca().yaxis.grid(True)
plt.xlabel("t")
plt.ylabel("wealth")
plt.yscale("log")
plt.plot((data[0,]), color='green')
plt.plot((data[1,]), color='red')
plt.plot((data[2,]), color='magenta', linestyle='dashed')
plt.plot((data[3,]), color='blue')
plt.plot((data[4,]), color='yellow')

# saving the first image
plt.savefig('thesis - kelly criterion.png')

'''
plotting the rate of growth of capital as function of f. One sees right away
that the optimal share is at 0.25
'''
# x stands for the share f
x = np.linspace(-0.2,1)

# y stands for the long-run exponential growth rate
y = 0.5 * np.log(1-x*0.4) + 0.5 * np.log(1 + x*0.5)

# adjusting the settings in order to properly display the function
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# displaying a vertical intercept at the optimal value of x (i.e. of f)
plt.axvline(x=0.25, linestyle='dashed')
plt.xlabel("f")
plt.ylabel("G")

# plotting the function
plt.plot(x,y, 'r')

# saving the second image
plt.savefig('thesis - optimal leverage.png')