def expMod(nombre, puissance, modulo): # Exponentiation modulaire
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