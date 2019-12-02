# Montrer qu'avec des nombres (très) petits, les clés sont craquables très facilement
# Et qu'avec des nombres petits (mais un peu plus grand), c'est déjà plus compliqué

from time import time
from logDiscret import discreteLogarithm

keyList = [((661, 23, 566), 7), ((4162261, 657413, 3473042), 844123), ((593465507, 543465507, 218967648), 513465507)]

for i in range (0, len(keyList)):
    publicKey = keyList[i][0]
    privateKey = keyList[i][1]

    print("\nESSAIE N° " + str(i + 1) + "\n\nSoit une clé publique " + str(publicKey) + " et une clé secrète " + str(privateKey))
    print("Essayons de trouver la clé secrète à partir de la clé publique via un algorithme de log discret\n")
    start = time()
    try:
        res = discreteLogarithm(publicKey[1], publicKey[2], publicKey[0]) # On trouve la clé secrète qui est 7
        end = time()
        print("Clé secrète trouvée en " + str(end-start) + " ms, et de valeur " + str(res) + "\n")
    except MemoryError:
        print("ERREUR : Pas assez de RAM (Nécessite Python 64 bits)")