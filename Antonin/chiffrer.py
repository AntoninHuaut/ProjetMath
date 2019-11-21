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
    print(clePublic)
    nPremier = clePublic[0]
    m = clePublic[1]
    k = randint(0, nPremier - 1)
    k = 13 # TEST comme modèle

    y1 = m**k % nPremier
    print(y1)
    

    for bloc in listBloc:
        return