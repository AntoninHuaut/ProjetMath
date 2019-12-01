import chiffrer
import dechiffrer
import genKeys

print("\nGENERATION CLES")
genKeys.genere_cle_Alice()
print("    Clé Alice:")
print("        Privé = " + str(genKeys.priveAlice))
print("        Public = " + str(genKeys.publicAlice))

# Situation de Bob qui envoie un message à Alice
print("\nENCODAGE")
msg = "Salut mon groupe de maths" # Msg a envoyé à l'autre personne
msgConverti = chiffrer.convertirMsg(msg)
listBloc = chiffrer.decoupageBloc(msgConverti)
print("    Message = " + msg + "   Converti = " + msgConverti)
print("    ListBloc = " + str(listBloc))

encodListBloc = chiffrer.encoderListBloc(genKeys.publicAlice, listBloc)
print("    ListBloc chiffré = " + str(encodListBloc))


# Situation d'Alice qui reçoit le message de Bob
print("\nDECODAGE")
listBloc = dechiffrer.decoderListBloc(
    encodListBloc, genKeys.publicAlice, genKeys.priveAlice)
print("    ListBloc déchiffré = " + str(listBloc))
print("    Message converti = " + str(dechiffrer.convertirMsg(listBloc)))
