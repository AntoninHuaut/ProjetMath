# coding: utf8
from random import *
from time import *
import math

def temoin(n,a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d /= 2
        s += 1
    print(int(d), s)
    return True

def nbPremier(k):
    puissanceMin = math.pow(10, 7)
    puissanceMax = math.pow(10, 8)
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    for i in range(k):
        a = randint(2, n-2)
        if temoin(n, a):
            print("pas premier")
            return n
    print("surement premier")
    return n

def tempsPremier():
    temps = 0
    n = 100
    for i in range(n):
        debut = time()
        p = nbPremier(100)
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%, nombre : ", p)
        temps += fin - debut
    return temps / n


print("Generation du nombre premier...")
p = nbPremier(100)
print("Nombre premier : ", p)
#print("calcul du temps moyen...")
#print("temps moyen : ", tempsPremier(), " s")
