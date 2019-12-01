from random import randint
import utils

# Converti une chaîne de caractère en chaîne de caractère de nombres
def convertirMsg(msg):
    mBytes = msg.encode("utf-8")
    mInt = int.from_bytes(mBytes, byteorder="big")
    return str(mInt)

# Transforme un nombre en list de bloc de 3 nombres
def decoupageBloc(msgConverti):
    listBloc = []

    # Pour chaque chiffre
    for numStr in msgConverti:
        # Initialisation au début
        if (len(listBloc) == 0):
            listBloc.append(numStr)
            continue # On skip à la prochaine itération

        index = len(listBloc) - 1;
        bloc = listBloc[index]

        # Si le bloc n'est pas complété
        if (len(bloc) < 3):
            listBloc[index] = bloc + numStr
        # Si le bloc est plein, on en crée un nouveau
        else:
            listBloc.append(numStr)
            
    for bloc in listBloc:
        listBloc[listBloc.index(bloc)] = int(bloc)
    
    return listBloc

# Encode la liste de bloc avec une clé publique
def encoderListBloc(clePublic, listBloc):
    nPremier = clePublic[0]
    m = clePublic[1]
    n = clePublic[2]

    # Pour chaque bloc
    for bloc in listBloc:
        k = randint(0, nPremier - 1)

        y1 = utils.expMod(m, k, nPremier)
        y2 = bloc * utils.expMod(n, k, nPremier) % nPremier
        newBloc = (y1, y2)
        
        listBloc[listBloc.index(bloc)] = newBloc

    return listBloc