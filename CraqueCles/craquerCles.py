from time import *
from logDiscret import discreteLogarithm

print("Soit une clé publique (661, 23, 566) et une clé secrète 7")
print("Essayons de trouver la clé secrète à partir de la clé publique via un algorithme de log discret\n")
start = time()
res = discreteLogarithm(23, 566, 661) # On trouve la clé secrète qui est 7
end = time()
print("Clé secrète trouvée en " + str(end-start) + " ms, et de valeur " + str(res))

# start = time()
# res = discreteLogarithm(2013, 831, 1073741823)
# end = time()
# print(str(res) + " en " + str(end-start) + " ms")