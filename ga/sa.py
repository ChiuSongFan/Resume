from random import *
from initial import initial, totally, get_neighbor_solution
from time import perf_counter
from fitness import monte_carlo
from numba import jit
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle
from numba import jit
data = pd.read_csv('data.csv')
kind = pd.read_csv('totallykind.csv')
c= data['c'].tolist()
amount = kind['ks'].tolist()
arc = kind['arc'].tolist()
cs = data['r'].tolist()
B = 1500
demand= 10
rep = 100
itertime= 10
@jit
def sa():
    for picture in range(1,31):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            cost, kind, componentr  = totally(ini, c, amount,cs)
            mc = monte_carlo(rep, demand, data, componentr, ini)
            test = mc.simulation()
            fitness = test
            if cost > B:
                fitness =0
            if fitness<1:
                break
        best = ini
        bestvalue = fitness
        bestcost = cost
        bestkind = kind
        gen=[]
        end= 0
        start = perf_counter()  
        while end-start < itertime:
            while 1:
                newini= get_neighbor_solution(ini)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                mc = monte_carlo(rep, demand, data, ncomponentr, newini)
                test1 = mc.simulation()
                newfitness = test1
                if cost > B:
                    newfitness = 0
                if newfitness<1:
                    break
            if newfitness >= bestvalue:
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            elif random() <= math.e**((newfitness-bestvalue)/T):
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            T*=R
            gen.append(bestvalue)
            start = start
            end= perf_counter()
        print(best,bestvalue,bestcost,bestkind,len(gen),end-start)
        gen.sort()
        time = np.linspace(0, 100 , len(gen))

        plt.plot(time,gen,label="SA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SA100/R{}.png'.format(picture))
        plt.close()

print(sa())
#把刻度改
