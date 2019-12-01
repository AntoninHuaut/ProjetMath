import utils


# Déchiffre une liste de bloc
def decoderListBloc(encodListBloc, clePublic, clePrivee):
    nPremier = clePublic[0]
    listBloc = []

    # Pour chaque bloc
    for bloc in encodListBloc:
        y1 = bloc[0]
        y2 = bloc[1]

        puissance = nPremier - 1 - clePrivee
        x = y2 * utils.expMod(y1, puissance, nPremier) % nPremier

        listBloc.append(x)

    return listBloc

# Converti une liste de bloc d'entier en chaîne de caractères
def convertirMsg(listBloc):
    msgList = ""
    count = 0

    # Pour chaque bloc
    for bloc in listBloc:
        blocStr = str(bloc)

        # Si le bloc a moins de 3 chiffres
        if count < len(listBloc) - 1:
            # On rajoute 0 devant le nombre tant qu'il n'a pas 3 chiffres
            while len(blocStr) < 3:
                blocStr = "0" + blocStr

        msgList += blocStr
        count += 1

    # On converti la chaîne de nombres en chaîne de caractère
    msgInt = int(msgList)
    mBytes = msgInt.to_bytes(((msgInt.bit_length() + 7) // 8), byteorder="big")
    m = mBytes.decode("utf-8")
    return m
