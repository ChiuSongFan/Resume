from random import *
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import accumulate
from numba import jit

class monte_carlo():
    def __init__(self,rep , d, data, r, w):
        self.rep =rep
        self.d = d
        self.data= data
        self.r = r
        self.w = w
    def simulation(self):
        rep =self.rep
        d = self.d
        data= self.data
        r = self.r
        w = self.w 
        success=0 
        z=[]
        for times in range(1,rep+1):
            #1
            u = [random() for _ in range(int(sum(w)))]
            #2       
            xi=0
            yi = [u[int(xi):int(xi)+int(k)] for xi, k in zip([0]+list(accumulate(w[:-1])), w)]
            #3
            yia = []   
            yiat = []
            for num,value in enumerate(yi):
                for l in value:
                    if l > r[num]:
                        yia.append(0)
                    else:
                        yia.append(1)
            y=0
            for m in w:
                yiat.append(yia[int(y):int(y)+int(m)])
                y+=m

            #
            #算出yi
            x =[sum(n) for n in yiat]
            #判斷v(kj)是否滿足d
            my_list = [x[0],x[1]+x[2],x[2]+x[3],x[3]+x[4],x[4]+x[5]+x[6],x[9]+x[10],x[10]+x[11],x[11]+x[12]+x[15],x[12]+x[13]+x[15],x[13]+x[14]+x[15],x[11]+x[14]+x[15],x[10]+x[13],x[9]+x[12]+x[15],x[9]+x[14]+x[15],x[4]+x[6]+x[7],x[4]+x[6]+x[8],x[2]+x[5]+x[6],x[2]+x[6]+x[7],x[2]+x[6]+x[8],x[1]+x[4]]
            if all(k >= d for k in my_list): 
                success=success+1
        return success/rep

if __name__ == '__main__':
    import io
    import sys
    import math
    import time
    from initial import initial,totally
    from numba import jit
    import numpy as np
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    data = pd.read_csv('data.csv')
    kind = pd.read_csv('totallykind.csv')
    #輸入所有元件成本和元件可靠度
    cost, cs= data['c'].tolist(), data['r'].tolist()
    #輸入arc之數量和在arc中能配置之元件種類各個數量
    amount, arc = kind['ks'].tolist(), kind['arc'].tolist()
    rep, demand = 2000 ,10
    for j in [500,1000,2000]:
        times=[]
        re=[]
        for i in range(100):
            Rsys=[]
            start = perf_counter()
            ini= [16, 20, 15, 9, 5, 3, 14, 14, 13, 16, 15, 6, 12, 3, 19, 19]
            Final = totally(ini, cost, amount,cs)
            budget, componentkind, componentr = totally(ini, cost, amount,cs)
            MCs = monte_carlo(j, demand, data, componentr, ini)
            end= perf_counter()
            times.append(end-start)
            re.append(MCs.simulation())
        print(j,sum(re)/len(re),sum(times)/len(times), np.std(re))
    # @jit
    # def main():
    #     d=6
    #     result = []
    #     start=time.time()
    #     for i in range(1,501):
    #         ini= [5,3,2,3,5,3,5,4,3,5,2,3,5,3,5,2,3,5,3,5,4,3,5,2,3,2,3,5,3,5]
    #         budget = totally(ini, c)
            
    #         mc = monte_carlo(i, d, data, r, ini)
            
    #         result.append(mc.simulation()[0])
    #     end = time.time()  
    #     time1 = np.linspace(0, 500,len(result))
    #     std = np.std(result[-200:])
    #     print(sum(result)/len(result),std,end-start)
    #     reliability=[sum(result)/len(result) for x in range(500)]
    #     plt.plot(time1,result)
    #     plt.plot(time1,reliability,'r--')
    #     plt.xlabel('Monte Carlo trials')
    #     plt.ylabel('System Reliability')
    #     plt.show()
    # for rep in [100,1000,3000,5000]:
    #     d=10
    #     MCs = 489
    #     ini= initial(c)
    #     mc = monte_carlo(rep, d, data, r, ini, MCs, MC) 
    #     start=time.time()
    #     print(mc.simulation())
    #     end = time.time() 
    #     print(end-start)
    
# repetition = [i for i in range(1,5001)]
# Rsys=[]
# for rep in repetition:
#     mc = monte_carlo(rep, d, data, a, r, up, c)
#     Rsys.append(mc.simulation())
# plt.plot(repetition,Rsys,color='r',linestyle='dashed',linewidth = 2)
# plt.xlabel('# of trials')
# plt.ylabel('system reliability')
# plt.show()