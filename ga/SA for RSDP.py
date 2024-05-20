from random import *
from initial import initial, totally, get_neighbor_solution
from multiprocessing import Process
import pandas as pd
from initial import initial, totally
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
import math
from DMCwithRSDP import SystemReliability,calculate_component_list
from numba import jit
data = pd.read_csv('data.csv')
kind = pd.read_csv('totallykind.csv')
c= data['c'].tolist()
amount = kind['ks'].tolist()
arc = kind['arc'].tolist()
cs = data['r'].tolist()
B = 1500
Demand = 10
rep = 1000                           
itertime= 600
pos =[[0],[1,2],[2,3],[3,4],[4,5,6],[9,10],[10,11],[11,12,15],[12,13,15],[13,14,15],[11,14,15],[10,13],[9,12,15],[9,14,15],[4,6,7],[4,6,8],[2,5,6],[2,6,7],[2,6,8],[1,4]]
@jit
def loop1():
    file = open("C:/Users/a1999/Desktop/實驗/SARSDP/sa.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            K = [[ini[0]],[ini[1],ini[2]],[ini[2],ini[3]],[ini[3],ini[4]],[ini[4],ini[5],ini[6]],[ini[9],ini[10]],[ini[10],ini[11]],[ini[11],ini[12],ini[15]],[ini[12],ini[13],ini[15]],[ini[13],ini[14],ini[15]],[ini[11],ini[14],ini[15]],[ini[10],ini[13]],[ini[9],ini[12],ini[15]],[ini[9],ini[14],ini[15]],[ini[4],ini[6],ini[7]],[ini[4],ini[6],ini[8]],[ini[2],ini[5],ini[6]],[ini[2],ini[6],ini[7]],[ini[2],ini[6],ini[8]],[ini[1],ini[4]]]
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                Componentlist = calculate_component_list(ini)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,ini, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                test = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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
                newini= get_neighbor_solution(ini)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                if ncost <= B:
                    Componentlist = calculate_component_list(newini)
                    s = SystemReliability(Componentlist)
                    DMC = SystemReliability.generate_DMC(s,newini, pos, Demand, K)
                    Demandlist =SystemReliability.find_upperboundary(s,DMC)
                    test1 = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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

        plt.plot(time,gen,label="SA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SARSDP/R{}.png'.format(picture))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind} {len(gen)}\n")
    file.close()
    return
@jit
def loop2():
    file = open("C:/Users/a1999/Desktop/實驗/SARSDP/sa2.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            K = [[ini[0]],[ini[1],ini[2]],[ini[2],ini[3]],[ini[3],ini[4]],[ini[4],ini[5],ini[6]],[ini[9],ini[10]],[ini[10],ini[11]],[ini[11],ini[12],ini[15]],[ini[12],ini[13],ini[15]],[ini[13],ini[14],ini[15]],[ini[11],ini[14],ini[15]],[ini[10],ini[13]],[ini[9],ini[12],ini[15]],[ini[9],ini[14],ini[15]],[ini[4],ini[6],ini[7]],[ini[4],ini[6],ini[8]],[ini[2],ini[5],ini[6]],[ini[2],ini[6],ini[7]],[ini[2],ini[6],ini[8]],[ini[1],ini[4]]]
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                Componentlist = calculate_component_list(ini)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,ini, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                test = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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
                newini= get_neighbor_solution(ini)
                ncost, nkind, ncomponentr  = totally(newini, c, amount,cs)
                if ncost <= B:
                    Componentlist = calculate_component_list(newini)
                    s = SystemReliability(Componentlist)
                    DMC = SystemReliability.generate_DMC(s,newini, pos, Demand, K)
                    Demandlist =SystemReliability.find_upperboundary(s,DMC)
                    test1 = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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

        plt.plot(time,gen,label="SA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SARSDP/R{}.png'.format(picture+10))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind}\n")
    file.close()
    return
@jit
def loop3():
    file = open("C:/Users/a1999/Desktop/實驗/SARSDP/sa3.txt", "w")
    for picture in range(1,11):
        T = 1
        R = 0.95
        while 1:
            ini= initial(arc)
            K = [[ini[0]],[ini[1],ini[2]],[ini[2],ini[3]],[ini[3],ini[4]],[ini[4],ini[5],ini[6]],[ini[9],ini[10]],[ini[10],ini[11]],[ini[11],ini[12],ini[15]],[ini[12],ini[13],ini[15]],[ini[13],ini[14],ini[15]],[ini[11],ini[14],ini[15]],[ini[10],ini[13]],[ini[9],ini[12],ini[15]],[ini[9],ini[14],ini[15]],[ini[4],ini[6],ini[7]],[ini[4],ini[6],ini[8]],[ini[2],ini[5],ini[6]],[ini[2],ini[6],ini[7]],[ini[2],ini[6],ini[8]],[ini[1],ini[4]]]
            cost, kind, componentr  = totally(ini, c, amount,cs)
            if cost <= B:
                Componentlist = calculate_component_list(ini)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,ini, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                test = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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
                    Componentlist = calculate_component_list(newini)
                    s = SystemReliability(Componentlist)
                    DMC = SystemReliability.generate_DMC(s,newini, pos, Demand, K)
                    Demandlist =SystemReliability.find_upperboundary(s,DMC)
                    test1 = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
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

        plt.plot(time,gen,label="SA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/SARSDP/R{}.png'.format(picture+20))
        plt.close()
        file.write(f"{best} {bestvalue} {bestcost} {bestkind} {len(gen)}\n")
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
