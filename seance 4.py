def compteur():
    n = 0
    while n<100:
        print(n)
        n+=1
def CompteurFor(n):
     for k in range(100):
          print(k)
try:
     argument = int(input("donne moi un chiffre"))
     CompteurFor(argument)
except ValueError:
        print("erreur")