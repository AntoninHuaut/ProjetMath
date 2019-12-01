from random import randint
import utils

def convertirMsg(msg):
    mBytes = msg.encode("utf-8")
    mInt = int.from_bytes(mBytes, byteorder="big")
    return str(mInt)

def decoupageBloc(msgConverti):
    listBloc = []

    for numStr in msgConverti:
        if (len(listBloc) == 0):
            listBloc.append(numStr)
            continue

        index = len(listBloc) - 1;
        bloc = listBloc[index]

        if (len(bloc) < 3):
            listBloc[index] = bloc + numStr
        else:
            listBloc.append(numStr)
            
    for bloc in listBloc:
        listBloc[listBloc.index(bloc)] = int(bloc)
    
    return listBloc

def encoderListBloc(clePublic, listBloc):
    nPremier = clePublic[0]
    m = clePublic[1]
    n = clePublic[2]

    for bloc in listBloc:
        k = randint(0, nPremier - 1)

        y1 = utils.expMod(m, k, nPremier)
        y2 = bloc * utils.expMod(n, k, nPremier) % nPremier
        newBloc = (y1, y2)
        
        listBloc[listBloc.index(bloc)] = newBloc

    return listBloc