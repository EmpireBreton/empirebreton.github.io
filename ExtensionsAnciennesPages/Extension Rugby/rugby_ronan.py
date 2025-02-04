from random import *
from math import *
from time import *

PouleB = ["Bretagne","Ecosse", "USA", "Pays de Galles"]
PouleB = ["Irlande","France","Angleterre", "Russie"]

NiveauPouleA = [10,8,7,7]
NiveauPouleB = [9,9,8,6]

Poule="B"
if Poule=="A":
    Equipe1 = int(input(f"Equipe 1 : [1 {PouleA[0]} - 2 {PouleA[1]} - 3 {PouleA[2]} - 4 {PouleA[3]}]?"))
    Equipe2 = int(input(f"Equipe 2 : [1 {PouleA[0]} - 2 {PouleA[1]} - 3 {PouleA[2]} - 4 {PouleA[3]}]?"))
    équipe1=PouleA[Equipe1-1]
    NiveauEquipe1 = NiveauPouleA[Equipe1-1]
    équipe2=PouleA[Equipe2-1]
    NiveauEquipe2 = NiveauPouleA[Equipe2-1]
else:
    Equipe1 = int(input(f"Equipe 1 : [1 {PouleB[0]} - 2 {PouleB[1]} - 3 {PouleB[2]} - 4 {PouleB[3]}]?"))
    Equipe2 = int(input(f"Equipe 2 : [1 {PouleB[0]} - 2 {PouleB[1]} - 3 {PouleB[2]} - 4 {PouleB[3]}]?"))
    équipe1=PouleB[Equipe1-1]
    NiveauEquipe1 = NiveauPouleB[Equipe1-1]
    équipe2=PouleB[Equipe2-1]
    NiveauEquipe2 = NiveauPouleB[Equipe2-1]




probabilitéEssais=8
probabilitéPénalité=120
probabilitéPenalitéEntre=2
probabilitéTransformation=1

ScoreEquipe1=0
ScoreEquipe2=0

for i in range (1,80):
    essaisEquipe1=randint(1,12//(NiveauEquipe1)+20)
    if essaisEquipe1 == probabilitéEssais:
        ScoreEquipe1 += 5
        print("Essais de : ", équipe1)
        transformationEquipe1=randint(1,2)
        if transformationEquipe1==probabilitéTransformation:
            ScoreEquipe1+=2
            print("Transformation de ", équipe1)
    
    essaisEquipe2=randint(1,12//(NiveauEquipe2)+20)
    if essaisEquipe2==probabilitéEssais:
        ScoreEquipe2 +=5
        print("Essais de ", équipe2)
        transformationEquipe2=randint(1,2)
        if transformationEquipe2==probabilitéTransformation:
            ScoreEquipe2+=2
            print("Transformation de ", équipe2)
    
    penaliteEquipe1=randint(1,200//(NiveauEquipe1))
    if penaliteEquipe1 == probabilitéPénalité:
        pénalitéEntréEquipe1=randint(1,2)
        if pénalitéEntréEquipe1==probabilitéPenalitéEntre:
            ScoreEquipe1+=3
    
    penaliteEquipe2=randint(1,200//(NiveauEquipe2))
    if penaliteEquipe2 == probabilitéPénalité:
        pénalitéEntréEquipe2=randint(1,2)
        if pénalitéEntréEquipe2==probabilitéPenalitéEntre:
            ScoreEquipe2+=3


    print(i,"minute","[",équipe1, ":", ScoreEquipe1,"||",équipe2,":", ScoreEquipe2,"]")
    if i == 40:
        print("-------------")
        print("   MI TEMPS  ")
        print("-------------")
        sleep(30)
    sleep(2)


if ScoreEquipe1 > ScoreEquipe2 :
    print("Victoire de : ", équipe1)

elif ScoreEquipe2 > ScoreEquipe1:
    print("Victoire de : ", équipe2)

else:
    print("Egalité")