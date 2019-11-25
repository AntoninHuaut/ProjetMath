# coding: utf8
import sys
sys.path.append("../Antonin")
from utils import expMod
from random import *
from time import *
import math
from sys import argv

def nbPremier(puissanceMin, puissanceMax):
    p = randint(puissanceMin, puissanceMax)
    while p % 2 == 0:
        p = randint(puissanceMin, puissanceMax)
    n = 3
    sqrt = math.sqrt(p)
    while n <= sqrt:
        if (p / n).is_integer():
            p = randint(puissanceMin, puissanceMax)
            while p % 2 == 0:
                p = randint(puissanceMin, puissanceMax)
            sqrt = math.sqrt(p)
            n = 3
        else:
            n += 2
    return p

def tempsPremier():
    puissanceMin = math.pow(10, int(argv[1]))
    puissanceMax = math.pow(10, int(argv[2]))
    temps = 0
    n = 100
    for i in range(n):
        debut = time()
        p = nbPremier(puissanceMin, puissanceMax)
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%, nombre : ", p)
        temps += fin - debut
    return temps / n

print("calcul du temps moyen...")
print("temps moyen : ", tempsPremier(), " s")
