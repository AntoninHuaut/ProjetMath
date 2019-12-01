import utils


def decoderListBloc(encodListBloc, clePublic, clePrivee):
    nPremier = clePublic[0]
    listBloc = []

    for bloc in encodListBloc:
        y1 = bloc[0]
        y2 = bloc[1]

        puissance = nPremier - 1 - clePrivee
        x = y2 * utils.expMod(y1, puissance, nPremier) % nPremier

        listBloc.append(x)

    return listBloc


def convertirMsg(listBloc):
    msgList = ""
    count = 0
    for bloc in listBloc:
        blocStr = str(bloc)

        if count < len(listBloc) - 1:
            while len(blocStr) < 3:
                blocStr = "0" + blocStr

        msgList += blocStr
        count += 1

    msgInt = int(msgList)
    mBytes = msgInt.to_bytes(((msgInt.bit_length() + 7) // 8), byteorder="big")
    m = mBytes.decode("utf-8")
    return m
