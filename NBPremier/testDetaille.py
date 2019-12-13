# Algorythme de test de Miller-Rabin. Arguments : 
# -ordre de grandeur min du nombre à générer
# -ordre de grandeur max du nombre à générer
# -précision (entre 1 et 80)
# -nombre de nombres premier à générer

# coding: utf8
import sys
sys.path.append("../ElGamal")
from utils import expMod
from random import *
from time import *
import math
from sys import argv

def temoin(n,a):  #Vérifie si l'entier a est un témoin de n
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
        print("temoin n° ", i, " : ", a, "\npour le nombre ", n, "\n")
        if temoin(n, a):
            return False #n est composé
    return True #n à une probabilité de 4**-k d'être composé

def nbPremier(puissanceMin, puissanceMax, precision): #Effectue le test de Miller-Rabin sur des nombres tirés aléatoirement jusqu'à avoir un nombre premier
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
    return n #nombre premier

def tempsPremier(): #Enregistre les nombres générés dans un fichier txt et leur temps de génération
    fichier =  open("nbPremier.txt", "a")
    puissanceMin = 10**int(argv[1])
    puissanceMax = 10**int(argv[2])
    precision = int(argv[3])
    nombre = int(argv[4])
    fichier.write("\n\nnombres d'ordre 10^" + argv[1] + "\nProbabilite de ne pas etre premier : " + str(4**(-int(precision))))
    temps = 0
    n = nombre
    for i in range(n):
        debut = time()
        p = nbPremier(puissanceMin, puissanceMax, precision)
        fin = time()
        print("nombre : ", p)
        temps += fin - debut
        fichier.write("\n" + str(p) + " en " + str(round(temps, 5)) + " s")


tempsPremier()