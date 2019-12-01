# Algorythme de test de Miller-Rabin.

# coding: utf8
import sys
sys.path.append("../ElGamal")
from utils import expMod
from random import *
from time import *
import math
from sys import argv

def temoin(n,a): #Vérifie si l'entier a est un témoin de n
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d//2
        s += 1
    x = expMod(a, d, n)
    for i in range(s):
        xi = x**2 % n 
        if xi == 1 and x !=1 and x != n-1:
            return True #a est témoin de n donc n est composé
        x = xi
    if x != 1:
        return True
    return False #n est probablement premier

def millerRabin(n, k): #effectue le test de Miller-Rabin pour k témoins
    for i in range(k):
        a = randint(2, n-2)
        if temoin(n, a):
            return False #n est composé
    return True #n à une probabilité de 4**-k d'être composé

def nbPremier(puissanceMin, puissanceMax, precision): #Effectue le test de Miller-Rabin sur des nombres tirés aléatoirement jusqu'à avoir un nombre premier
    puissanceMin = 10**puissanceMin
    puissanceMax = 10**puissanceMax
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    while not millerRabin(n, precision):
        n = randint(puissanceMin, puissanceMax)
        while n % 2 == 0:
            n = randint(puissanceMin, puissanceMax)
    return n #nombre premier

