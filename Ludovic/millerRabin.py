# coding: utf8
import sys
sys.path.append("../Antonin")
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
        if temoin(n, a):
            return False
    return True

def nbPremier(puissanceMin, puissanceMax, precision):
    puissanceMin = 10**puissanceMin
    puissanceMax = 10**puissanceMax
    n = randint(puissanceMin, puissanceMax)
    while n % 2 == 0:
        n = randint(puissanceMin, puissanceMax)
    while not millerRabin(n, precision):
        n = randint(puissanceMin, puissanceMax)
        while n % 2 == 0:
            n = randint(puissanceMin, puissanceMax)
    return n

