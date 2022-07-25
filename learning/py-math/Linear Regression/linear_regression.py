import numpy as np
import matplotlib.pyplot as plt



x = np.array([0.1,0.4,0.30,0.45,0.5,0.55,0.90])
y =          [0.1,0.2,0.3 ,0.4 ,0.5,0.6 ,0.7]

#print(x)
#print(y)

plt.scatter(y, x, c='red')

wagi=0
bias=0

def koszt(wagi, bias, x, wartos_prawdziwa):
	predykcja = x*wagi+bias # y=wx+b
	MSE  = (1/len(y)) * np.sum(np.square(wartos_prawdziwa-predykcja))
	return MSE

def spadek_gradientu(x, y, lr, iteracje):
    bias = 0
    wagi = 0.1 
    
    for n in range(iteracje):
        predykcja = x * wagi + bias  

        dw = 1/len(x) * np.sum((-2*x*(predykcja - y)))
        db = 1/len(x) * np.sum(2*(predykcja - y))
        
        wagi = wagi - lr * dw
        bias = bias - lr * db
        
        if n % 30 == 0:
            print("Loss : ",koszt(wagi,bias,x,y))
            
    return wagi, bias  
wagi,bias = spadek_gradientu(x,y,0.2,150)
predykcja = x * wagi + bias         
plt.scatter(y,x,c="red")
plt.plot(predykcja,x,c="green")


from IPython.display import clear_output
import time 

for i in range(0,150):
    plt.figure()
    wagi,bias = spadek_gradientu(x,y,0.2,i)
    predykcja = x * wagi + bias         
    plt.scatter(y,x,c="red")
    plt.plot(predykcja,x,c="green")
    plt.show()
    time.sleep(0.15)
    
    clear_output(wait=True)