def Rugby(PaysA="PaysA", IndexA=10, PaysB="PaysB", IndexB=10):
    """Match de Rugby, 80 minutes sans prolongations."""
    from os import name
    from os import system
    from random import randint
    from time import sleep
    system('cls' if name == 'nt' else 'clear')

    print("COUPE DU MONDE 🏉🏆")
    VariableQuiSertARien=input()
    Pays=[PaysA, PaysB]
    Index=[IndexA,IndexB] # Index de Force


    print(f"Match : {Pays[0]} - {Pays[1]}")
    print("-----------------")
    score=[0, 0]

    print("PREMIÈRE MI-TEMPS")
    for i in range(0,41):
        x=randint(Index[0], 100)
        y=randint(Index[1], 100)

        # PENALITES
        if x-1==Index[0]:
            print(f"Pénalité de {Pays[0]} !")
            score[0]+=3
        if y-1==Index[1]:
            print(f"Pénalité de {Pays[1]} !")
            score[1]+=3
        
        # ESSAIS
        if x==Index[0]:
            print(f"🏉 ESSAI DE {Pays[0].upper()}")
            score[0]+=5
            if randint(0,1)==0: # TRANSFORMATIONS (A)
                score[0]+=2
                print(f"🏉 Transformation de {Pays[0]}")
        if y==Index[1]:
            print(f"🏉 ESSAI DE {Pays[1].upper()}")
            score[1]+=5
            if randint(0,1)==0: # TRANSFORMATIONS (B)
                score[1]+=2
                print(f"🏉 Transformation de {Pays[1]}")

        if i<10:
            print(f"0{i}' : {score}")
        elif i<40 and i>9:
            print(f"{i}' : {score}")
        sleep(1)

    print("-----------------")
    print("MI-TEMPS")
    sleep(15)
    print("-----------------")

    print("SECONDE MI-TEMPS")
    tempsadditionnel=randint(0, 6)
    for i in range(40,81):
        x=randint(Index[0], 100)
        y=randint(Index[1], 100)

        # PENALITES
        if x-1==Index[0]:
            print(f"Pénalité de {Pays[0]} !")
            score[0]+=3
        if y-1==Index[1]:
            print(f"Pénalité de {Pays[1]} !")
            score[1]+=3
        
        # ESSAIS
        if x==Index[0]:
            print(f"🏉 ESSAI DE {Pays[0].upper()}")
            score[0]+=5
            if randint(0,1)==0: # TRANSFORMATIONS (A)
                score[0]+=2
                print(f"🏉 Transformation de {Pays[0]}")
        if y==Index[1]:
            print(f"🏉 ESSAI DE {Pays[1].upper()}")
            score[1]+=5
            if randint(0,1)==0: # TRANSFORMATIONS (B)
                score[1]+=2
                print(f"🏉 Transformation de {Pays[1]}")
        if i<90:
            print(f"{i}' : {score}")
        sleep(1)

    # RESULTATS
    print("---------")
    print(score)
    if score[0]>score[1]:
        print(f"Victoire de {Pays[0]}")
        return Pays[0], score
    elif score[1]>score[0]:
        print(f"Victoire de {Pays[1]}")
        return Pays[1], score
    else:
        print("Match Nul !")
        return None, score

def Foot(PaysA="PaysA", IndexA=10, PaysB="PaysB", IndexB=10):
    from os import name
    from os import system
    from random import randint
    from time import sleep
    system('cls' if name == 'nt' else 'clear')
    print("COUPE DU MONDE ⚽️🏆")

    VariableQuiSertARien=input()



    Pays=[PaysA, PaysB]
    Index=[IndexA,IndexB] # Index de Force


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

def FootProlongations(PaysA="PaysA", IndexA=10, PaysB="PaysB", IndexB=10):
    from os import name
    from os import system
    from random import randint
    from time import sleep
    system('cls' if name == 'nt' else 'clear')
    print("COUPE DU MONDE ⚽️🏆")

    VariableQuiSertARien=input()



    Pays=[PaysA, PaysB]
    Index=[IndexA,IndexB] # Index de Force




    print("Match Éliminatoire : {} - {}".format(Pays[0], Pays[1]))
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
        print("PREMIÈRE PROLONGATION")
        tempsadditionnel=randint(0, 3)
        for i in range(90,106+tempsadditionnel): # première mi-temps
            x=randint(Index[0], 100)
            y=randint(Index[1], 100)
            
            if x==Index[0]:
                print("⚽️ BUT DE", Pays[0].upper())
                score[0]=score[0]+1
            if y==Index[1]:
                print("⚽️ BUT DE", Pays[1].upper())
                score[1]=score[1]+1

            if i==105:
                print("Temps Additionnel :", tempsadditionnel)
            elif i<105:
                print("{}' : {}".format(i, score))
            else:
                print("105+{}' : {}".format(i-105, score))
            sleep(1)

        print("-----------------")
        print("MI-TEMPS")
        sleep(15)
        print("-----------------")

        print("SECONDE PROLONGATION")
        tempsadditionnel=randint(0, 3)
        for i in range(105,121+tempsadditionnel): # deuxième mi-temps
            x=randint(Index[0], 100)
            y=randint(Index[1], 100)
            
            if x==Index[0]:
                print("⚽️ BUT DE", Pays[0].upper())
                score[0]=score[0]+1
            if y==Index[1]:
                print("⚽️ BUT DE", Pays[1].upper())
                score[1]=score[1]+1
            if i<120:
                print("{}' : {}".format(i, score))
            else:
                print("120+{}' : {}".format(i-120, score))
            if i==120:
                print("Temps Additionnel :", tempsadditionnel)
            sleep(1)
        print("---------")
        if score[0]>score[1]:
            print("Victoire de", Pays[0])
        elif score[1]>score[0]:
            print("Victoire de", Pays[1])
        else:
            TirAuButA=[]
            TirAuButB=[]
            for i in range(5):
                print("Tir de {} :".format(Pays[0]))
                sleep(5)
                if randint(1, 2)==1:
                    TirAuButA.append("🟢")
                    print("     Pénalty Réussi de {}".format(Pays[0]))
                else:
                    TirAuButA.append("🔴")
                    print("     Pénalty Raté de {}".format(Pays[0]))
                print("Tir de {} :".format(Pays[1]))
                sleep(5)
                if randint(1, 2)==1:
                    TirAuButB.append("🟢")
                    print("     Pénalty Réussi de {}".format(Pays[0]))
                else:
                    TirAuButB.append("🔴")
                    print("     Pénalty Raté de {}".format(Pays[1]))
                print("--------------")
                print("{} : {}\n{} : {}".format(Pays[0],TirAuButA, Pays[1], TirAuButB))
                print("--------------")
            if TirAuButA.count("🟢")==TirAuButB.count("🟢"):
                print("PASSAGE AU TIR AU BUT ELMINATOIRE")
            while TirAuButA.count("🟢")==TirAuButB.count("🟢"):
                print("Tir de {} :".format(Pays[0]))
                sleep(5)
                if randint(1, 2)==1:
                    TirAuButA.append("🟢")
                    print("     Pénalty Réussi de {}".format(Pays[0]))
                else:
                    TirAuButA.append("🔴")
                    print("     Pénalty Raté de {}".format(Pays[0]))
                print("Tir de {} :".format(Pays[1]))
                sleep(5)
                if randint(1, 2)==1:
                    TirAuButB.append("🟢")
                    print("     Pénalty Réussi de {}".format(Pays[0]))
                else:
                    TirAuButB.append("🔴")
                    print("     Pénalty Raté de {}".format(Pays[0]))
                print("--------------")
                print("{} : {}\n{} : {}".format(Pays[0],TirAuButA, Pays[1], TirAuButB))
                print("--------------")
            if TirAuButA.count("🟢")>TirAuButB.count("🟢"):
                print("Victoire de", Pays[0])
            elif TirAuButA.count("🟢")<TirAuButB.count("🟢"):
                print("Victoire de", Pays[1])
    print("Score du Match {} / {} : {}-{}".format(Pays[0], Pays[1], score[0], score[1]))
    if score[0]==score[1]:
        print("Prolongations : {}-{}".format(TirAuButA.count("🟢"), TirAuButB.count("🟢")))

def Tennis(PaysA="PaysA", IndexA=10, PaysB="PaysB", IndexB=10):
    """Match de Tennis avec points d'écart."""
    from os import name
    from os import system
    from random import randint
    from time import sleep
    system('cls' if name == 'nt' else 'clear')

    print("COUPE DU MONDE 🎾🏆")
    VariableQuiSertARien=input()
    Pays=[PaysA, PaysB]
    Index=[IndexA,IndexB] # Index de Force


    print(f"Match : {Pays[0]} - {Pays[1]}")
    print("-----------------")
    score=[0, 0]
    ecart=[False, False]
    gagnant=False

    while gagnant==False:
        x=0
        y=0
        while x==y:
            x=randint(Index[0], 100)
            y=randint(Index[1], 100)
        
        if x>y:
            print(f"Point de {Pays[0]}")
            if score[0]<30:
                score[0]+=15
            elif score[0]==30:
                score[0]+=10
            elif score==40:
                if ecart[0]==False:
                    ecart[0]=True
                else:
                    if ecart[1]==False:
                        gagnant=0
                    else:
                        ecart[0]=False
                        ecart[1]=False
        elif y>x:
            print(f"Point de {Pays[1]}")
            if score[1]<30:
                score[1]+=15
            elif score[1]==30:
                score[1]+=10
            elif score==40:
                if ecart[1]==False:
                    ecart[1]=True
                else:
                    if ecart[0]==False:
                        gagnant=1
                    else:
                        ecart[0]=False
                        ecart[1]=False

        if score[0]!=40 or score[1]!=40:
            print(f"Score : {score[0]} - {score[1]}")
        else:
            print(f"Score : {score[0]} ({str(ecart[0]).replace('True', 'A').replace('False', '/')})- {score[1]} ({str(ecart[1]).replace('True', 'A').replace('False', '/')})")
        input()
    # RESULTATS
    print("---------")
    print(score)
    print(f"Le gagnant est {Pays[gagnant]}")
    return Pays[gagnant], score, ecart


# Appels des fonctions
Tennis("Medvedev (RU)", 10, "Nadal (ES)", 9)