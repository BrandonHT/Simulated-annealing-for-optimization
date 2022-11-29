# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:11:04 2022

@author: brand
"""

import math
import numpy as np

def annealing_schedule(t):
    return 0.9*t

def ackley(a=20, b=0.2, c=2*3.14159):
    def ackley_implementation(x):
        d = len(x)
        return -a*math.exp(-b*math.sqrt(sum(np.power(x, 2)/d))) - math.exp(sum(math.cos(c*xi) for xi in x)/d) + a + math.exp(1)
    return ackley_implementation

def parabola():
    def parabola_x2_1(x):
        return sum(np.power(np.subtract(x,1), 2))
    return parabola_x2_1

def cos_x2():
    def cos_x2_imp(x):
        return sum(np.power(x, 2))
    return cos_x2_imp

def simulated_annealing(f=ackley, x=10, T=None, t=annealing_schedule, k_max=1000, temp=100):
    y = f([x])
    x_best, y_best = x, y
    for k in range(k_max):
        delta_x = np.random.uniform(-2,2)   
        x_new = x + delta_x
        y_new = f([x_new])
        delta_y = y_new - y
        temp = annealing_schedule(temp)
        selecting = np.random.uniform()
        if delta_y <= 0 or selecting < math.exp(-delta_y/temp):
            x, y = x_new, y_new
        if y_new < y_best:
            x_best, y_best = x_new, y_new
    return x_best

print(simulated_annealing(
    f=parabola(), 
    x=2, 
    T=None, 
    t=annealing_schedule, 
    k_max=100, 
    temp=10)
)