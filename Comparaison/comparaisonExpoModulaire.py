# Script permettant de comparer le temps de calcul entre a^b [c] de façon naïve et via l'exponentiation modulaire

import sys
sys.path.append("../ElGamal")
from utils import expMod
from time import time

start = time()
res1 = pow(5631219912, 91122) % 72
end = time()
print("\n Méthode classique en " + str(end-start) + " ms")

start = time()
res2 = expMod(5631219912, 91122, 72)
end = time()
print("\n Exponentiation modulaire en " + str(end-start) + " ms")

memeRes = "oui" if res1 == res2 else "non"
print("\n Même résultat = " + memeRes)
