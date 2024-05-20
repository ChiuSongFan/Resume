from random import randint,choice,sample
import numpy as np
def initial(c):
    number = randint(1, 4)
    multiple = 5 * number
    return [randint(0, multiple) for i in c]
#改成多元件並記錄員件種類，成本跟元件可靠度有差改下
def totally(arc, cost, amount, componentreliability):
    findkinds, totallycost, kinds, cr = [], [], [], []
    cut = 0
    for i, amt in enumerate(amount):
        aw = cost[cut:cut+amt]
        rd = choice(aw)
        findkinds.append(rd)
        kinds.append(aw.index(rd) + 1)
        ca = componentreliability[cut:cut+amt]
        cr.append(ca[aw.index(rd)])
        cut += amt
    for j, ar in enumerate(arc):
        totallycost.append(findkinds[j] * ar)
    return sum(totallycost), kinds, cr

if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import random 
    from time import perf_counter
    data = pd.read_csv('data.csv')
    kind = pd.read_csv('totallykind.csv')
    cost= data['c'].tolist()
    amount = kind['ks'].tolist()
    arc = kind['arc'].tolist()
    cs = data['r'].tolist()
    for i in range(10):
        ini= initial(arc)
        print(ini)