# Algorithme d'exponentiation modulaire
# On calcule le résultat au fur à mesure de la division par 2
def expMod(nombre, puissance, modulo):
    p = puissance
    sumRes = nombre
    res = 1
    while p >= 1:
        resMod = p % 2

        # Si le bit est à 0, il ne compte pas pour le résultat final
        if resMod == 1:
            res *= sumRes
            res %= modulo

        p = p // 2
        sumRes = sumRes ** 2 % modulo

    return res