def compteur1():
    nombre_final = int(input("choisir le nombre final : "))
    n = 0
    while n <= nombre_final:
        print(n)
        n += 1
compteur1()









def compteur2():
    nombre_final = int(input("choisir le nombre final : "))
    n = 0
    while n < nombre_final:
        n += 1
        print(n)
compteur2()












def compteur(nombre_final):
    n = 0
    while n <= nombre_final:
        print(n)
        n += 1
compteur(5)






def compteur3(nombre_final, valeur_depart):
    n = valeur_depart
    while n <= nombre_final:
        print(n)
        n += 1
compteur3(50,5)









def compteur4(nombre_final, valeur_depart, pas):
    n = valeur_depart
    while n <= nombre_final:
        print(n)
        n += pas
compteur4(50,5,1)









def compteur5(nombre_final, valeur_depart, pas):
    n = valeur_depart
    while n <= nombre_final:
        print(n)
        n += pas

v = [50, 4, 2]
compteur5(v[0], v[1], v[2])


