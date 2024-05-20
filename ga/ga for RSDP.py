from multiprocessing import Process
import pandas as pd
from initial import initial, totally
from fitness import monte_carlo
from selection import select
from crossandmutation import crossover, mutate
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
from DMCwithRSDP import SystemReliability,calculate_component_list
from numba import jit
def best(x):
	return x[3]
def evaluate_chromosome(fitnesslist, costlist, budget):
    Rmax = 0.99
    Rmin = 0.01
    for i, j in enumerate(fitnesslist):
        fitness = fitnesslist[i]
        cost = costlist[i]
        if fitness >1:
            fitness =Rmax
        if cost > budget:
            fitness = Rmin**((cost/budget)**0.5)
        fitnesslist[i] = fitness
    return fitnesslist	
data = pd.read_csv('data.csv')
kind = pd.read_csv('totallykind.csv')
#輸入所有元件成本和元件可靠度
c, cs= data['c'].tolist(), data['r'].tolist()
#輸入arc之數量和在arc中能配置之元件種類各個數量
amount, arc = kind['ks'].tolist(), kind['arc'].tolist()
budget = 1500
Demand = 10
rep = 1000                           
pop_size = 150
pc = 0.9			
pm = 0.09
Iterationtime = 600
num_splits = 8
pos =[[0],[1,2],[2,3],[3,4],[4,5,6],[9,10],[10,11],[11,12,15],[12,13,15],[13,14,15],[11,14,15],[10,13],[9,12,15],[9,14,15],[4,6,7],[4,6,8],[2,5,6],[2,6,7],[2,6,8],[1,4]]
@jit
def loop1():
    file = open("C:/Users/a1999/Desktop/實驗/GARSDP/ga.txt", "w")
    for picture in range(1,11):
        pop = []
        end=0
        start=perf_counter()
        bestfitness = []
        while len(pop) < pop_size:	
            M = initial(arc)
            K = [[M[0]],[M[1],M[2]],[M[2],M[3]],[M[3],M[4]],[M[4],M[5],M[6]],[M[9],M[10]],[M[10],M[11]],[M[11],M[12],M[15]],[M[12],M[13],M[15]],[M[13],M[14],M[15]],[M[11],M[14],M[15]],[M[10],M[13]],[M[9],M[12],M[15]],[M[9],M[14],M[15]],[M[4],M[6],M[7]],[M[4],M[6],M[8]],[M[2],M[5],M[6]],[M[2],M[6],M[7]],[M[2],M[6],M[8]],[M[1],M[4]]]
            pop.append(M)
        start = perf_counter()
        while end-start < Iterationtime:
            fitness= []
            costlist= []
            kindlist= []
            for offspring in pop:
                cost, kind, componentr  = totally(offspring, c, amount,cs)
                Componentlist = calculate_component_list(offspring)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,offspring, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                value = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
                fitness.append(value)
                costlist.append(cost)
                kindlist.append(kind)
            fitness = evaluate_chromosome(fitness, costlist, budget)
            best_fitness_index = fitness.index(max(fitness))
            best_fitness_value = fitness[best_fitness_index]
            best_fitness_cost = costlist[best_fitness_index]
            best_fitness_kind = kindlist[best_fitness_index]
            best_fitness_pop = pop[best_fitness_index]
            bestfitness.append([best_fitness_pop, best_fitness_kind, best_fitness_cost, best_fitness_value])
            new_population = []
            while len(new_population) < pop_size:
                parent1 = select(pop, fitness)
                parent2 = select(pop, fitness)
                child1, child2  = crossover(parent1[0], parent2[0], pc, num_splits)
                child1,  child2 = mutate(child1, pm), mutate(child2, pm)
                new_population.append(child1)
                new_population.append(child2)
            pop = new_population
            end = perf_counter()
        bestsolution =  max(bestfitness, key=best)
        draw=[]
        time = np.linspace(0, 600 ,len(bestfitness))
        for i in range(len(bestfitness)):
            draw.append(bestfitness[i][3])
        draw.sort()
        plt.plot(time,draw,color='red',label="GA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/GARSDP/R{}.png'.format(picture))
        plt.close()
        file.write(f"{bestsolution} {len(bestfitness)}\n")
    file.close()
    return
@jit
def loop2():
    file = open("C:/Users/a1999/Desktop/實驗/GARSDP/ga2.txt", "w")
    for picture in range(1,11):
        pop = []
        end=0
        start=perf_counter()
        bestfitness = []
        while len(pop) < pop_size:	
            M = initial(arc)
            K = [[M[0]],[M[1],M[2]],[M[2],M[3]],[M[3],M[4]],[M[4],M[5],M[6]],[M[9],M[10]],[M[10],M[11]],[M[11],M[12],M[15]],[M[12],M[13],M[15]],[M[13],M[14],M[15]],[M[11],M[14],M[15]],[M[10],M[13]],[M[9],M[12],M[15]],[M[9],M[14],M[15]],[M[4],M[6],M[7]],[M[4],M[6],M[8]],[M[2],M[5],M[6]],[M[2],M[6],M[7]],[M[2],M[6],M[8]],[M[1],M[4]]]
            pop.append(M)
        start = perf_counter()
        while end-start < Iterationtime:
            fitness= []
            costlist= []
            kindlist= []
            for offspring in pop:
                cost, kind, componentr  = totally(offspring, c, amount,cs)
                Componentlist = calculate_component_list(offspring)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,offspring, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                value = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
                fitness.append(value)
                costlist.append(cost)
                kindlist.append(kind)
            fitness = evaluate_chromosome(fitness, costlist, budget)
            best_fitness_index = fitness.index(max(fitness))
            best_fitness_value = fitness[best_fitness_index]
            best_fitness_cost = costlist[best_fitness_index]
            best_fitness_kind = kindlist[best_fitness_index]
            best_fitness_pop = pop[best_fitness_index]
            bestfitness.append([best_fitness_pop, best_fitness_kind, best_fitness_cost, best_fitness_value])
            new_population = []
            while len(new_population) < pop_size:
                parent1 = select(pop, fitness)
                parent2 = select(pop, fitness)
                child1, child2  = crossover(parent1[0], parent2[0], pc, num_splits)
                child1,  child2 = mutate(child1, pm), mutate(child2, pm)
                new_population.append(child1)
                new_population.append(child2)
            pop = new_population
            end = perf_counter()
        bestsolution =  max(bestfitness, key=best)
        draw=[]
        time = np.linspace(0, 600 ,len(bestfitness))
        for i in range(len(bestfitness)):
            draw.append(bestfitness[i][3])
        draw.sort()
        plt.plot(time,draw,color='red',label="GA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/GARSDP/R{}.png'.format(picture+10))
        plt.close()
        file.write(f"{bestsolution} {len(bestfitness)}\n")
    file.close()
    return
@jit
def loop3():
    file = open("C:/Users/a1999/Desktop/實驗/GARSDP/ga3.txt", "w")
    for picture in range(1,11):
        pop = []
        end=0
        start=perf_counter()
        bestfitness = []
        while len(pop) < pop_size:	
            M = initial(arc)
            K = [[M[0]],[M[1],M[2]],[M[2],M[3]],[M[3],M[4]],[M[4],M[5],M[6]],[M[9],M[10]],[M[10],M[11]],[M[11],M[12],M[15]],[M[12],M[13],M[15]],[M[13],M[14],M[15]],[M[11],M[14],M[15]],[M[10],M[13]],[M[9],M[12],M[15]],[M[9],M[14],M[15]],[M[4],M[6],M[7]],[M[4],M[6],M[8]],[M[2],M[5],M[6]],[M[2],M[6],M[7]],[M[2],M[6],M[8]],[M[1],M[4]]]
            pop.append(M)
        start = perf_counter()
        while end-start < Iterationtime:
            fitness= []
            costlist= []
            kindlist= []
            for offspring in pop:
                cost, kind, componentr  = totally(offspring, c, amount,cs)
                Componentlist = calculate_component_list(offspring)
                s = SystemReliability(Componentlist)
                DMC = SystemReliability.generate_DMC(s,offspring, pos, Demand, K)
                Demandlist =SystemReliability.find_upperboundary(s,DMC)
                value = SystemReliability.rsdp_reliability(s,Demandlist,Componentlist)
                fitness.append(value)
                costlist.append(cost)
                kindlist.append(kind)
            fitness = evaluate_chromosome(fitness, costlist, budget)
            best_fitness_index = fitness.index(max(fitness))
            best_fitness_value = fitness[best_fitness_index]
            best_fitness_cost = costlist[best_fitness_index]
            best_fitness_kind = kindlist[best_fitness_index]
            best_fitness_pop = pop[best_fitness_index]
            bestfitness.append([best_fitness_pop, best_fitness_kind, best_fitness_cost, best_fitness_value])
            new_population = []
            while len(new_population) < pop_size:
                parent1 = select(pop, fitness)
                parent2 = select(pop, fitness)
                child1, child2  = crossover(parent1[0], parent2[0], pc, num_splits)
                child1,  child2 = mutate(child1, pm), mutate(child2, pm)
                new_population.append(child1)
                new_population.append(child2)
            pop = new_population
            end = perf_counter()
        bestsolution =  max(bestfitness, key=best)
        draw=[]
        time = np.linspace(0, 600 ,len(bestfitness))
        for i in range(len(bestfitness)):
            draw.append(bestfitness[i][3])
        draw.sort()
        plt.plot(time,draw,color='red',label="GA")
        plt.ylim(0,1.2)
        plt.legend()
        plt.savefig('C:/Users/a1999/Desktop/實驗/GARSDP/R{}.png'.format(picture+20))
        plt.close()
        file.write(f"{bestsolution} {len(bestfitness)}\n")
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