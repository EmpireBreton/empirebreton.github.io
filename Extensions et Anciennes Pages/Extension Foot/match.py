from os import name
from os import system
from random import randint
from time import sleep
system('cls' if name == 'nt' else 'clear')
print("COUPE DU MONDE ⚽️🏆")

VariableQuiSertARien=input()



Pays=["Ukraine", "Russie"]
Index=[10,9] # Index de Force


print("Match de Poule : {} - {}".format(Pays[0], Pays[1]))
print("-----------------")
score=[0, 0]

print("PREMIÈRE MI-TEMPS")
tempsadditionnel=randint(0, 6)
for i in range(0,46+tempsadditionnel): # première mi-temps
    x=randint(Index[0], 100)
    y=randint(Index[1], 100)
    
    if x==Index[0]:
        print("⚽️ BUT DE", Pays[0].upper())
        score[0]=score[0]+1
    if y==Index[1]:
        print("⚽️ BUT DE", Pays[1].upper())
        score[1]=score[1]+1

    if i==45:
        print("Temps Additionnel :", tempsadditionnel)
    if i<10:
        print("0{}' : {}".format(i, score))
    elif i<45 and i>9:
        print("{}' : {}".format(i, score))
    else:
         print("45+{}' : {}".format(i-45, score))
    sleep(1)

print("-----------------")
print("MI-TEMPS")
sleep(15)
print("-----------------")

print("SECONDE MI-TEMPS")
tempsadditionnel=randint(0, 6)
for i in range(45,91+tempsadditionnel): # deuxième mi-temps
    x=randint(Index[0], 100)
    y=randint(Index[1], 100)
    
    if x==Index[0]:
        print("⚽️ BUT DE", Pays[0].upper())
        score[0]=score[0]+1
    if y==Index[1]:
        print("⚽️ BUT DE", Pays[1].upper())
        score[1]=score[1]+1
    if i<90:
        print("{}' : {}".format(i, score))
    else:
         print("90+{}' : {}".format(i-90, score))
    if i==90:
        print("Temps Additionnel :", tempsadditionnel)
    sleep(1)
print("---------")
print(score)
if score[0]>score[1]:
    print("Victoire de", Pays[0])
elif score[1]>score[0]:
    print("Victoire de", Pays[1])
else:
    print("Match Nul !")