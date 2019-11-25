def tempsPremier():
    fichier =  open("nbPremier.txt", "a")
    puissanceMin = 10**int(argv[1])
    puissanceMax = 10**int(argv[2])
    precision = int(argv[3])
    nombre = int(argv[4])
    fichier.write("\n\nnombres d'ordre 10^" + argv[1] + "\nProbabilite de ne pas etre premier : " + str(2**(-int(precision))))
    temps = 0
    n = nombre
    for i in range(n):
        debut = time()
        p = nbPremier(puissanceMin, puissanceMax, precision)
        fin = time()
        print(round(((i+n)/n-1)*100, 2), "%, nombre : ", p)
        temps += fin - debut
        fichier.write("\n" + str(p) + " en " + str(round(temps, 5)) + " s")
    return temps / n


