import chiffrer
import genKeys

genKeys.genere_cle_Alice()
msgChifree = chiffrer.convertirMsg("supinfo");
listBloc = chiffrer.decoupageBloc(msgChifree)
print(listBloc)
encodListBloc = chiffrer.encoderListBloc(genKeys.publicAlice, listBloc)
print(encodListBloc)