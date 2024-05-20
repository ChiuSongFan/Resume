from random import *
import numpy as np

def crossover(parent1, parent2, pc, num_splits):
    if np.random.random() < pc:
        positions = np.sort(np.random.choice(len(parent1), size=num_splits, replace=False))
        split_ranges = np.split(parent1, positions)
        child1_genes = []
        child2_genes = []
        for i in range(len(split_ranges)):
            if i % 2 == 0:
                child1_genes.extend(split_ranges[i])
                child2_genes.extend(np.split(parent2, positions)[i])
            else:
                child1_genes.extend(np.split(parent2, positions)[i])
                child2_genes.extend(split_ranges[i])
        child1 = list(child1_genes)
        child2 = list(child2_genes)
    else:
        child1, child2 = parent1.copy(), parent2.copy()
        
    return child1, child2
def mutate(child, pm):
    if random() < pm:
        idxs = sample(range(len(child)), k=12)
        for i in idxs:
            child[i] = randint(3, 20)
    return child

if __name__ == '__main__':
    import numpy as np
    from initial import *
    import pandas as pd
    from time import perf_counter
    kind = pd.read_csv('totallykind.csv')
    arc = kind['arc'].tolist()
    for i in range(10):
        a,s=initial(arc),initial(arc)
        cr = crossover(a,s, 1,10)
        mu = mutate(cr[0], 1)
        print(cr)