import random

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def getPrime(maxN):
    return list(filter(isPrime, range(1, maxN)));

def getRandomPrime(maxN):
    primeList = getPrime(maxN)
    return random.choice(primeList)