def expMod(nombre, puissance, modulo):  # Exponentiation modulaire
    p = puissance
    sumRes = nombre
    res = 1
    while p >= 1:
        resMod = p % 2

        if resMod == 1:
            res *= sumRes
            res %= modulo

        p = p // 2
        sumRes = sumRes ** 2 % modulo

    return res