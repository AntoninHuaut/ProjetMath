import sys
sys.path.append("../Ludovic")
from millerRabin import nbPremier
from utils import expMod
import prime
import random

global priveAlice
global publicAlice
priveAlice = 0
publicAlice = 0

def genere_cle():
    p = nbPremier(300, 301, 128) # (10^)100 car mini 100 de longueurs de précisions 128 (~ 3 * 10^-39 chance de non premier)

    a = random.randint(10**100, p - 2) # 100 car mini 100 de longueurs
    m = random.randint(10**100, p - 1) # 100 car mini 100 de longueurs
    n = expMod(m, a, p)

    return [a, (p, m, n)]


def genere_cle_Alice():
    global priveAlice
    global publicAlice
    res = genere_cle()
    priveAlice = res[0]
    publicAlice = res[1]
