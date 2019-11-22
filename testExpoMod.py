from time import *


def modpow(base, exp, m):
    result = 1

    while exp > 0:
        if (exp & 1) > 0:
            result = (result * base) % m
        exp >>= 1
        base = (base * base) % m

    return result


def expMod(nombre, puissance, modulo):  # Exponentiation modulaire
    p = puissance
    count = 0
    sumRes = 1
    while p >= 1:
        resMod = p % 2

        if resMod == 1:
            sumRes *= nombre ** (2 ** count)
            sumRes %= modulo

        p = p // 2
        count += 1

    return sumRes


start = time()
res1 = modpow(10 ^ 999999, 10 ^ 999999, 17)
end = time()
print("\n modpow fait en " + str(end-start) + " ms")

start = time()
res2 = expMod(10 ^ 999999, 10 ^ 999999, 17)
end = time()
print("\n expMod fait en " + str(end-start) + " ms")

print("\n Même résultat = " + str(res1 == res2))
