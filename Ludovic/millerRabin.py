# coding: utf8
import sys
sys.path.append("../Antonin")
from random import *
from time import *
import math
from sys import argv

def temoin(n,a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d//2
        s += 1
        x = pow(a, d, n) # Pourquoi plus puissant que exponentation modulaire
        for i in range(s):
            xi = x**2 % n 
            if xi == 1 and x !=1 and x != n-1:
                return True
            x = xi
        if x != 1:
            return True
    return False

def millerRabin(n, k):
    for i in range(k):
        a = randint(2, n-2)
        if temoin(n, a):
            return False
    return True

def nbPremier(puissanceMin, puissanceMax):
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    while not millerRabin(n, 1):
        n = randint(puissanceMin, puissanceMax)
        while n % 2 == 0:
            n = randint(puissanceMin, puissanceMax)
    return n

def tempsPremier():
    puissanceMin = 10**int(argv[1])
    puissanceMax = 10**int(argv[2])
    temps = 0
    n = 1000
    for i in range(n):
        debut = time()
        p = nbPremier(puissanceMin, puissanceMax)
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%, nombre : ", p)
        temps += fin - debut
    return temps / n


print("calcul du temps moyen...")
print("temps moyen : ", tempsPremier(), " s")
