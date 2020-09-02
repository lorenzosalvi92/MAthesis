# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:51:48 2019

@author: Lorenzo
"""
import numpy as np
import random
from matplotlib import pyplot as plt
#from pylab import rcParams
from collections import Counter
np.seterr(divide = 'ignore') 

# setting parameters
# number of trials
n = 10000
# probability of success
p = 0.5
# probability of failure
q = 0.5
# expected value
m = 5000
# standard deviation
sd = round(np.sqrt(n*p*q))
# fixed number of successes (expected value +/- a certain number of standard deviations)
successes = np.asarray([m-5*sd, round(m-4.5*sd), m-4*sd, round(m-3.5*sd), m-3*sd, round(m-2.5*sd), m-2*sd, round(m-1.5*sd), m-1*sd, round(m-0.5*sd), m, round(m+0.5*sd), m+1*sd, round(m+1.5*sd), m+2*sd, round(m+2.5*sd), m+3*sd, round(m+3.5*sd), m+4*sd, round(m+4.5*sd), m+5*sd])
coinflips = np.zeros((21,10000))

# create matrix with different streaks of successes and failures
for j in range(0,21):
        ones = np.ones((1,int(successes[j,])))
        zeros = np.zeros((1,int(n - successes[j,])))
        x = np.concatenate((ones, zeros), axis = 1)
        coinflips[j,:] = x
        random.shuffle(coinflips[j,:])

# test: check that number of 1s and 0s is correct
counter = Counter(coinflips[0,:])

# define interest rate
r = 0.01

# define "prior" Kelly fractions 
baseline_1 = (5/(5+5))*(1+r)*1/(0.4+r) - (1-(5/(5+5)))*(1+r)*1/(0.5-r)
baseline_2 = (6/(6+4))*(1+r)*1/(0.4+r) - (1-(6/(6+4)))*(1+r)*1/(0.5-r)
baseline_3 = (4/(6+4))*(1+r)*1/(0.4+r) - (1-(4/(6+4)))*(1+r)*1/(0.5-r)
baseline_4 = baseline_2*0.5
baseline_5 = baseline_3*0.5

#####################################################

data_bayesian_kelly55 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly55 = 100
    # starting optimal fraction 
    f_bayesian_kelly55 = 0.20
    # probability of winning (Beta distribution with parameters 4,4)
    a = 5
    b = 5
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly55 = X_bayesian_kelly55*(1+f_bayesian_kelly55*0.5+(1-f_bayesian_kelly55)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly55 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly55 = X_bayesian_kelly55*(1-f_bayesian_kelly55*0.4+(1-f_bayesian_kelly55)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly55 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly55[y,i] =  X_bayesian_kelly55

starting_value_bayesian_kelly55 = 100*np.ones((21,1))
data_bayesian_kelly55 = np.append(starting_value_bayesian_kelly55, data_bayesian_kelly55, axis = 1)
terminal_values_bayesian_kelly55 = np.log(data_bayesian_kelly55[:,10000])

#####################################################

data_1xkelly = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly = 100
    # starting optimal fraction 
    f_1xkelly = 0.2
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly = X_1xkelly*(1+f_1xkelly*0.5+(1-f_1xkelly)*r)
       else: 
           X_1xkelly = X_1xkelly*(1-f_1xkelly*0.4 +(1-f_1xkelly)*r)
       data_1xkelly[y,i] = X_1xkelly
   
starting_value_1xkelly = 100*np.ones((21,1))
data_1xkelly = np.append(starting_value_1xkelly, data_1xkelly, axis = 1)
terminal_values_1xkelly = np.log(data_1xkelly[:,10000])

#####################################################

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()            
plt.scatter(successes,terminal_values_bayesian_kelly55, color = 'red')
plt.scatter(successes,terminal_values_1xkelly, color = 'blue')

# saving the image
plt.savefig('thesis - bayesian kelly 5-5 vs kelly.png')

#####################################################

data_bayesian_kelly64 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly64 = 100
    # starting optimal fraction 
    f_bayesian_kelly64 = 0.65
    # probability of winning (Beta distribution with parameters 3,1)
    a = 6
    b = 4
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly64 = X_bayesian_kelly64*(1+f_bayesian_kelly64*0.5+(1-f_bayesian_kelly64)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly64 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly64 = X_bayesian_kelly64*(1-f_bayesian_kelly64*0.4+(1-f_bayesian_kelly64)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly64 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly64[y,i] =  X_bayesian_kelly64

starting_value_bayesian_kelly64 = 100*np.ones((21,1))
data_bayesian_kelly64 = np.append(starting_value_bayesian_kelly64, data_bayesian_kelly64, axis = 1)
terminal_values_bayesian_kelly64 = np.log(data_bayesian_kelly64[:,10000])

#####################################################

data_1xkelly_wo = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly_wo = 100
    # starting optimal fraction 
    f_1xkelly_wo = 0.65
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly_wo = X_1xkelly_wo*(1+f_1xkelly_wo*0.5+(1-f_1xkelly_wo)*r)
       else: 
           X_1xkelly_wo = X_1xkelly_wo*(1-f_1xkelly_wo*0.4 +(1-f_1xkelly_wo)*r)
       data_1xkelly_wo[y,i] = X_1xkelly_wo
   
starting_value_1xkelly_wo = 100*np.ones((21,1))
data_1xkelly_wo = np.append(starting_value_1xkelly_wo, data_1xkelly_wo, axis = 1)
terminal_values_1xkelly_wo = np.log(data_1xkelly_wo[:,10000])

#####################################################

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()            
plt.scatter(successes,terminal_values_bayesian_kelly55, color = 'red')
plt.scatter(successes,terminal_values_bayesian_kelly64, color = 'magenta')
plt.scatter(successes,terminal_values_1xkelly, color = 'blue')
plt.scatter(successes,terminal_values_1xkelly_wo, color = 'cyan')

# saving the image
plt.savefig('thesis - bayesian kelly 5-5 vs kelly (1).png')

#####################################################

data_bayesian_kelly46 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_bayesian_kelly46 = 100
    # starting optimal fraction 
    f_bayesian_kelly46 = -0.25
    # probability of winning (Beta distribution with parameters 3,1)
    a = 4
    b = 6
    sum_a_b = a + b
    p = a / sum_a_b
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_bayesian_kelly46 = X_bayesian_kelly46*(1+f_bayesian_kelly46*0.5+(1-f_bayesian_kelly46)*r)
           a = a + 1
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly46 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       else: 
           X_bayesian_kelly46 = X_bayesian_kelly46*(1-f_bayesian_kelly46*0.4+(1-f_bayesian_kelly46)*r)
           sum_a_b = sum_a_b + 1
           f_bayesian_kelly46 = (a/sum_a_b)*(1+r)*1/(0.4+r) - (1-a/sum_a_b)*(1+r)*1/(0.5-r)
       data_bayesian_kelly46[y,i] =  X_bayesian_kelly46

starting_value_bayesian_kelly46 = 100*np.ones((21,1))
data_bayesian_kelly46 = np.append(starting_value_bayesian_kelly46, data_bayesian_kelly46, axis = 1)
terminal_values_bayesian_kelly46 = np.log(data_bayesian_kelly46[:,10000])

#####################################################

data_1xkelly_wo1 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_1xkelly_wo1 = 100
    # starting optimal fraction 
    f_1xkelly_wo1 = -0.25
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_1xkelly_wo1 = X_1xkelly_wo1*(1+f_1xkelly_wo1*0.5+(1-f_1xkelly_wo1)*r)
       else: 
           X_1xkelly_wo1 = X_1xkelly_wo1*(1-f_1xkelly_wo1*0.4 +(1-f_1xkelly_wo1)*r)
       data_1xkelly_wo1[y,i] = X_1xkelly_wo1
   
starting_value_1xkelly_wo1 = 100*np.ones((21,1))
data_1xkelly_wo1 = np.append(starting_value_1xkelly_wo1, data_1xkelly_wo1, axis = 1)
terminal_values_1xkelly_wo1 = np.log(data_1xkelly_wo1[:,10000])

#####################################################

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()            
plt.scatter(successes,terminal_values_bayesian_kelly55, color = 'red')
plt.scatter(successes,terminal_values_bayesian_kelly46, color = 'magenta')
plt.scatter(successes,terminal_values_1xkelly, color = 'blue')
plt.scatter(successes,terminal_values_1xkelly_wo1, color = 'cyan')

# saving the image
plt.savefig('thesis - bayesian kelly 5-5 vs kelly (2).png')

#####################################################

data_halfkelly_wo = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_halfkelly_wo = 100
    # starting optimal fraction 
    f_halfkelly_wo = 0.65*0.5
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_halfkelly_wo = X_halfkelly_wo*(1+f_halfkelly_wo*0.5+(1-f_halfkelly_wo)*r)
       else: 
           X_halfkelly_wo = X_halfkelly_wo*(1-f_halfkelly_wo*0.4 +(1-f_halfkelly_wo)*r)
       data_halfkelly_wo[y,i] = X_halfkelly_wo
   
starting_value_halfkelly_wo = 100*np.ones((21,1))
data_halfkelly_wo = np.append(starting_value_halfkelly_wo, data_halfkelly_wo, axis = 1)
terminal_values_halfkelly_wo = np.log(data_halfkelly_wo[:,10000])

#####################################################

data_halfkelly_wo1 = np.zeros((21,10000))

for y in range(0,21):
    # starting capital
    X_halfkelly_wo1 = 100
    # starting optimal fraction 
    f_halfkelly_wo1 = -0.25*0.5
    for i in range(0,10000):
       if coinflips[y,i] == 1: 
           X_halfkelly_wo1 = X_halfkelly_wo1*(1+f_halfkelly_wo1*0.5+(1-f_halfkelly_wo1)*r)
       else: 
           X_halfkelly_wo1 = X_halfkelly_wo1*(1-f_halfkelly_wo1*0.4 +(1-f_halfkelly_wo1)*r)
       data_halfkelly_wo1[y,i] = X_halfkelly_wo1
   
starting_value_halfkelly_wo1 = 100*np.ones((21,1))
data_halfkelly_wo1 = np.append(starting_value_halfkelly_wo1, data_halfkelly_wo1, axis = 1)
terminal_values_halfkelly_wo1 = np.log(data_halfkelly_wo1[:,10000])

#####################################################

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()            
plt.scatter(successes,terminal_values_bayesian_kelly64, color = 'magenta')
plt.scatter(successes,terminal_values_1xkelly_wo, color = 'cyan')
plt.scatter(successes,terminal_values_halfkelly_wo, color = 'green')

# saving the image
plt.savefig('thesis - bayesian kelly 5-5 vs kelly (3).png')

#######################################################

plt.ylabel('logarithm of terminal wealth', fontdict=None, labelpad=None)
plt.xlabel('number of successes', fontdict=None, labelpad=None)   
plt.grid()            
plt.scatter(successes,terminal_values_bayesian_kelly46, color = 'magenta')
plt.scatter(successes,terminal_values_1xkelly_wo1, color = 'cyan')
plt.scatter(successes,terminal_values_halfkelly_wo1, color = 'green')

# saving the image
plt.savefig('thesis - bayesian kelly 5-5 vs kelly (4).png')