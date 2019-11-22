import chiffrer
import dechiffrer
import genKeys

print("\nGENERATION CLES")
genKeys.genere_cle_Alice()
print("    Clé Alice:")
print("        Privé = " + str(genKeys.priveAlice))
print("        Public = " + str(genKeys.publicAlice))

print("\nENCODAGE")
msg = "Salut mon groupe de maths"
msgConverti = chiffrer.convertirMsg(msg)
listBloc = chiffrer.decoupageBloc(msgConverti)
print("    Message = " + msg + "   Converti = " + msgConverti)
print("    ListBloc = " + str(listBloc))

encodListBloc = chiffrer.encoderListBloc(genKeys.publicAlice, listBloc)
print("    ListBloc chiffré = " + str(encodListBloc))


print("\nDECODAGE")
listBloc = dechiffrer.decoderListBloc(
    encodListBloc, genKeys.publicAlice, genKeys.priveAlice)
print("    ListBloc déchiffré = " + str(listBloc))
print("    Message converti = " + str(dechiffrer.convertirMsg(listBloc)))
