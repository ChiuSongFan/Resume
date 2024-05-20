if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import random 
    from time import perf_counter
    data = pd.read_csv('data.csv')
    kind = pd.read_csv('totallykind.csv')
    amount = kind['ks'].tolist()
    arc = kind['arc'].tolist()
    cs = data['r'].tolist()
    cost= [116800,58400,49056,57232,57232,11680,16352,21024,16352,42048,37376,28032,23360,18922,18922,25229,44968,32120,51392,66576,66576,46603,15885,15885,11914,14950,18688,19622,17170,11446,8410,7008,11213,16352,11446,5840,8176,10512]
    x = [2, 3, 1, 2, 1, 3, 1, 3, 3, 3, 3, 2, 3, 3, 2, 3]



    a1,cost1=[9, 10, 17, 8, 4, 2, 9, 1, 3, 2, 10, 19, 10, 7, 4, 15],[1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 3, 1, 1, 2]
    a_list = [a1]
    cost_list = [cost1]
    avg=[]
    for i in range(1):
        y = cost_list[i]
        z = [y[i] + sum(x[:i]) for i in range(len(y))]
        ini= a_list[i]
        test=[]
        for i in z:
            test.append(cost[i-1])
        tot = sum([a*b for a,b in zip(ini,test)])
        avg.append(tot)
    print(avg[0])
    print(sum(avg)/len(avg))
