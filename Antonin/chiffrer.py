from random import *

def convertirMsg(msg):
    msgChiffree = "";

    for lettre in msg:
        ordAlphabet = ord(lettre) - 96
        if (ordAlphabet < 10):
            ordAlphabet = "0" + str(ordAlphabet)
        
        msgChiffree += str(ordAlphabet)

    return msgChiffree

def decoupageBloc(msgChiffree):
    listBloc = []

    for numStr in msgChiffree:
        num = int(numStr)

        if (len(listBloc) == 0 and num == 0): continue # Si on commence par un 0, on ignore

        if (len(listBloc) == 0):
            listBloc.append(numStr)
            continue

        index = len(listBloc) - 1;
        bloc = listBloc[index]

        if (len(bloc) < 3):
            listBloc[index] = bloc + numStr
        else:
            listBloc.append(numStr)

    index = len(listBloc) - 1;
    while (len(listBloc[index]) < 3):
        listBloc[index] = listBloc[index] + "0"
    
    return listBloc

def encoderListBloc(clePublic, listBloc):
    nPremier = clePublic[0]
    m = clePublic[1]
    n = clePublic[2]

    for bloc in listBloc:
        blocEntier = int(bloc)
        k = randint(0, nPremier - 1)
        k = 13 # TEST comme modèle

        y1 = expMod(m, k, nPremier)
        y2 = blocEntier * expMod(n, k, nPremier) % nPremier
        y2 = (blocEntier * n**k) % nPremier
        newBloc = (y1, y2)
        
        listBloc[listBloc.index(bloc)] = newBloc

    return listBloc

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