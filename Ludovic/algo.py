# coding: utf8
from random import *
from time import *
import math

def nbPremier():
    cpt=0
    puissanceMin = math.pow(10, 12)
    puissanceMax = math.pow(10, 13)
    p = randint(puissanceMin, puissanceMax)
    while p % 2 == 0:
        p = randint(puissanceMin, puissanceMax)
    n = 3
    sqrt = math.sqrt(p)
    while n <= sqrt:
        if (p / n).is_integer():
            cpt = cpt + 1
            p = randint(puissanceMin, puissanceMax)
            while p % 2 == 0:
                p = randint(puissanceMin, puissanceMax)
            sqrt = math.sqrt(p)
            n = 3
        else:
            n += 2
    return p

def tempsPremier():
    temps = 0
    n = 100
    for i in range(n):
        debut = time()
        p = nbPremier()
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%")
        temps += fin - debut
    return temps / n

print("Generation du nombre premier...")
p = nbPremier()
print("Nombre premier : ", p)
print("calcul du temps moyen...")
print("temps moyen : ", tempsPremier(), " s")
