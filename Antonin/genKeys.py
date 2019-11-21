import prime
import random

global priveAlice
global publicAlice
priveAlice = 0
publicAlice = 0

def genere_cle():
    p = prime.getRandomPrime(1000)
    a = random.randint(1, p - 2)
    m = random.randint(1, p - 1)
    p = 661 # TEST comme modèle
    a = 7 # TEST comme modèle
    m = 23  # TEST comme modèle
    n = m**a % p

    return [a, (p, m, n)]


def genere_cle_Alice():
    global priveAlice
    global publicAlice
    res = genere_cle()
    priveAlice = res[0]
    publicAlice = res[1]
