#programmable 100% By Belhaj Ayman
#CPGE IBN GHAZI 
import numpy as np
import math as mt
import matplotlib.pyplot as plt
############# outils arithmetiques #####################
def est_premium(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True
def valuation_p_adique(p,n):
    s = 0
    while (n)%(p**s)==0:
        s +=1
    return s-1
def est_premium(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True
def decompo1(n):
    l =[]
    for i in range(2,n+1):
        if est_premium(i)==True:
            if valuation_p_adique(i,n)==0:
                continue
            else:
                l.append((i,valuation_p_adique(i,n)))
    return l
def is_int(n):
    if n-int(n)==0:
        return True
    else:
        return False
def est_carre_parfait(n):
    return is_int(np.sqrt(n))
def pair(n):
    if is_int(n/2)==True:
        return True
    return False
############# outils informatique #####################
def construction_arrays(array,f):
    A =[]
    for i in range(len(array)):
        A.append(f(array[i]))
    return A
############# outils analyse integrale #####################
def integrale(min,max,dx,f):
    '''min est la borne inf du fonction
       max est la borne sup du fonction
       dx est la precision  
       vous pouver changer la fct f(x)'''
    s = 0
    for i in np.arange(min,max,dx):
        s += dx*f(i)
    return s
############# outils algebre mobios #####################
def mobios1(n):
    for i in range(2,n-1):
        if est_carre_parfait(i)==True:
            if n%i==0:
                return True
    return False
def mobios2(n):
    array = decompo1(n)
    for i in range(len(array)):
        if array[i][1]>1:
            return False
    return True

def mobios3(n):
    array = decompo1(n)
    s = len(array)
    if pair(s)==True:
        return True
    return False
def mobios(n):
    if n==1:
        return 1
    if mobios1(n)==True:
        return 0
    if mobios2(n)==True:
        if mobios3(n)==True:
            return 1
        else:
            return -1
    else:
        return 0
############# les fonction #####################
def card(n):
    s = 0
    if n ==0:
        return 0
    for i in range(1,n):
        if est_premium(i)==True:
            s +=1
    return s
def approxima_log(x):
    if x ==0:
        return 0
    if x ==1:
        return 0
    else:
        return x/mt.log(x)
def li(x):
    return integrale(2,x,0.001,lambda t:1/mt.log(t))
def ri(x):
    s = 0
    for i in range(1,100):
        s += (mobios(i)*li(x**(1/i)))/i
    return s
############# les representation #####################
def show_mobios(n):
    x = list(range(1,n))
    mob = construction_arrays(x,mobios)
    plt.plot(x,mob,"ro",label="fonction-mobios u(x)")
    plt.legend()
    plt.show()
def show(n):
    x = list(range(2,n))
    y = list(range(2,n))
    z = list(range(2,n))
    gamma = list(range(2,n))
    array_app1 = construction_arrays(x,card)
    array_app2 = construction_arrays(y,approxima_log)
    array_app3 = construction_arrays(y,li)
    array_app4 = construction_arrays(y,ri)
    plt.plot(x,array_app1,label="nbre premier")
    plt.plot(y,array_app2,label="t/log(x)")
    plt.plot(z,array_app3,label="li(x)")
    plt.plot(gamma,array_app4,label="Ri(x)")
    plt.legend()
    plt.show()
############# des exapmles #####################
#show_mobios(20)
#show(200)