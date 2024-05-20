from random import *
from initial import initial, totally, get_neighbor_solution
from multiprocessing import Process
import pandas as pd
from initial import initial, totally
from fitness import monte_carlo
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
import math
from numba import jit
data = pd.read_csv('data.csv')
kind = pd.read_csv('totallykind.csv')
c= data['c'].tolist()
amount = kind['ks'].tolist()
arc = kind['arc'].tolist()
cs = data['r'].tolist()
B = 5000
demand = 10
rep = 1000                           
itertime= 600

@jit
def loop1():
    file = open("C:/Users/a1999/Desktop/實驗/SA100/sa.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                mc = monte_carlo(rep, demand, data, componentr, ini)
                test = mc.simulation()
                if test < 1:
                    fitness = test
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
                newini= initial(arc)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                if ncost <= B:
                    mc = monte_carlo(rep, demand, data, ncomponentr, newini)
                    test1 = mc.simulation()
                    if   test1 < 1:
                        newfitness = test1
                        break
            if newfitness >= bestvalue:
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            elif random() <= math.e**((newfitness-bestvalue)/T):
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            T*=R
            gen.append(bestvalue)
            start = start
            end= perf_counter()
        gen.sort()
        time = np.linspace(0, 600 , len(gen))

        plt.plot(time,gen,label="SA100")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SA100/R{}.png'.format(picture))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind}\n")
    file.close()
    return
@jit
def loop2():
    file = open("C:/Users/a1999/Desktop/實驗/SA100/sa2.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                mc = monte_carlo(rep, demand, data, componentr, ini)
                test = mc.simulation()
                if test < 1:
                    fitness = test
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
                newini= initial(arc)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                if ncost <= B:
                    mc = monte_carlo(rep, demand, data, ncomponentr, newini)
                    test1 = mc.simulation()
                    if   test1 < 1:
                        newfitness = test1
                        break
            if newfitness >= bestvalue:
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            elif random() <= math.e**((newfitness-bestvalue)/T):
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            T*=R
            gen.append(bestvalue)
            start = start
            end= perf_counter()
        gen.sort()
        time = np.linspace(0, 600 , len(gen))

        plt.plot(time,gen,label="SA100")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SA100/R{}.png'.format(picture+10))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind}\n")
    file.close()
    return
@jit
def loop3():
    file = open("C:/Users/a1999/Desktop/實驗/SA100/sa3.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                mc = monte_carlo(rep, demand, data, componentr, ini)
                test = mc.simulation()
                if test < 1:
                    fitness = test
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
                newini= initial(arc)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                if ncost <= B:
                    mc = monte_carlo(rep, demand, data, ncomponentr, newini)
                    test1 = mc.simulation()
                    if   test1 < 1:
                        newfitness = test1
                        break
            if newfitness >= bestvalue:
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            elif random() <= math.e**((newfitness-bestvalue)/T):
                best, bestvalue, bestcost, bestkind  = newini, newfitness, ncost, nkind
            T*=R
            gen.append(bestvalue)
            start = start
            end= perf_counter()
        gen.sort()
        time = np.linspace(0, 600 , len(gen))

        plt.plot(time,gen,label="SA100")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SA100/R{}.png'.format(picture+20))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind}\n")
    file.close()
    return
if __name__ == '__main__':
    # 創建兩個線程
    t1 = Process(target=loop1)
    t2 = Process(target=loop2)
    t3 = Process(target=loop3)
    # 開始執行線程
    t1.start()
    t2.start()
    t3.start()
    # 等待兩個線程結束
    t1.join()
    t2.join()
    t3.join()
