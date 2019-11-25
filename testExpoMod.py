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
    sumRes = nombre
    res = 1
    while p >= 1:
        resMod = p % 2

        if resMod == 1:
            res *= sumRes
            res %= modulo

        p = p // 2
        sumRes = sumRes ** 2 % modulo
        count += 1

    return res

start = time()
res1 = modpow(10 ^ 999999, 10 ^ 999999, 17)
end = time()
print("\n modpow fait en " + str(end-start) + " ms")

start = time()
res2 = expMod(10 ^ 999999, 10 ^ 999999, 17)
end = time()
print("\n expMod fait en " + str(end-start) + " ms")

print("\n Même résultat = " + str(res1 == res2))
