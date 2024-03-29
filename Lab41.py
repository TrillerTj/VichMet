import math
import matplotlib.pyplot as plt
from matplotlib import mlab
import pandas as pd

 
 
# начальные условия
x0 = 0
y0 = 1
xn = 1


 
 
f = lambda x, y: y * math.cos(x)
N = 100
for k in range(100,1000):
    N = 1
    N +=k
    h = (xn - x0) / float(N)
    ilist = mlab.frange(0, 20, 1)
    xlist = [(x0+h*i) for i in ilist]
    ylist = []
 
 
    prev = y0
    for x in xlist:
        y = prev + h*f(x,y0)
        prev = y
        ylist.append(prev)
 
      
    lst = []
    for x in xlist:
        func = math.e ** math.sin(x)
        lst.append(func)
 
    
    flag = True
    raz = [] 
    for i in range(len(xlist)):
        raz.append(math.fabs(ylist[i]-lst[i]))
        if raz[i] > 0.01:
            flag = False
            break
    print
   
    
    if flag == True:
         
        plt.rc('font',**{'family':'verdana'})
        plt.xlabel("ось абцисс")
        plt.ylabel("ось ординат")
        plt.plot(xlist, ylist, "g-", label="метод Эйлера")
        plt.plot(xlist, lst, "r-", label="точное решение")
        plt.legend()
        plt.grid()
        plt.show()
        print (N)
        table1 = {"x": xlist, "f(x)": lst, "f(x')": ylist, "raz":raz }
        df1 = pd.DataFrame(data=table1)
        df1 = df1.round({"x": 5, "f(x)": 5, "f(x')":5, "raz":5})
        print('\n', df1)
        break
            