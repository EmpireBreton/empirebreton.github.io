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

# Appels des fonctions
Rugby("Ukraine", 10, "Russie", 9)