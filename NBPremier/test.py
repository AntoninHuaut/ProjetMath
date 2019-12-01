# coding: utf8
import sys
sys.path.append("../ElGamal")
from utils import expMod
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
    x = expMod(a, d, n)
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
        print("temoin n° ", i, " : ", a, "\npour le nombre ", n, "\n")
        if temoin(n, a):
            return False
    return True

def nbPremier(puissanceMin, puissanceMax, precision):
    cpt = 0
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    while not millerRabin(n, precision):
        print("nombre composé, nouvel essai")
        cpt += 1
        n = randint(puissanceMin, puissanceMax)
        while n % 2 == 0:
            n = randint(puissanceMin, puissanceMax)
    print("Nombres générés avant de trouver un nombre premier : ", cpt)
    return n

def tempsPremier():
    fichier =  open("nbPremier.txt", "a")
    puissanceMin = 10**int(argv[1])
    puissanceMax = 10**int(argv[2])
    precision = int(argv[3])
    nombre = int(argv[4])
    fichier.write("\n\nnombres d'ordre 10^" + argv[1] + "\nProbabilite de ne pas etre premier : " + str(2**(-int(precision))))
    temps = 0
    n = nombre
    for i in range(n):
        debut = time()
        p = nbPremier(puissanceMin, puissanceMax, precision)
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%, nombre : ", p)
        temps += fin - debut
        fichier.write("\n" + str(p) + " en " + str(round(temps, 5)) + " s")


tempsPremier()