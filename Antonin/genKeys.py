import prime
import random

global priveAlice
global publicAlice
priveAlice = 0
publicAlice = 0

def genere_cle():
    p = 0
    
    while p < 1000: # p doit être supérieur au nombre contenu dans chaque bloc. Les blocs étant par 3, ils peuvent atteindre 999. Donc p doit être minimum égal à 1000
        p = prime.getRandomPrime(5000)

    a = random.randint(1, p - 2)
    m = random.randint(1, p - 1)
    n = m**a % p

    return [a, (p, m, n)]


def genere_cle_Alice():
    global priveAlice
    global publicAlice
    res = genere_cle()
    priveAlice = res[0]
    publicAlice = res[1]
