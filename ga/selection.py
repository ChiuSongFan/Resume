from numpy import *

def select(pop, fitness):
    if all(f == 0 for f in fitness):
        min_sum_index = argmin([sum(p) for p in pop])
        return pop[min_sum_index], fitness[min_sum_index]
    
    sum_fitness = sum(fitness)
    probabilities = [f/sum_fitness for f in fitness]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_num = random.random()
    
    for i in range(len(cumulative_probabilities)):
        if random_num < cumulative_probabilities[i]:
            return pop[i], fitness[i]
if __name__ == '__main__':
    import random
    import pandas as pd
    from initial import *
    from fitness import monte_carlo
    data=pd.read_csv('data.csv')
    c, B = data['c'].tolist(), 10000
    r= data['r'].tolist()
    rep = 100
    pop = []
    fitness = []
    cost =[]
    data = pd.read_csv('data.csv')
    kind = pd.read_csv('totallykind.csv')
    amount = kind['ks'].tolist()
    arc = kind['arc'].tolist()
    demand=5
    for i in range(10):
        ini= initial(arc)
        budget, kind, componentr  = totally(ini, c, amount,c)
        mc = monte_carlo(rep, demand, data, componentr, ini)
        a=mc.simulation()
        cost.append(budget)
        pop.append(ini)
        fitness.append(a)
    for j in range(10):
        s = select(pop, fitness)
        print(cost)
        print(s)