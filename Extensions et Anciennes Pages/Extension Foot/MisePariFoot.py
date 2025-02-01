CoteFr=1.23
CoteNul=6.90
CoteAu=12.50
Mise=float(input("Mise="))
Gagnant=int(input("Avez vous eu le gagnant exact ? [0NON-1OUI]"))
ScoreExact=int(input("Avez vous eu le score exact ? [0NON-1OUI]"))

PaysGagnant=str(input("Pays Gagnant ? [FR-NUL-AU]"))
if PaysGagnant=='FR' or PaysGagnant=='fr' or PaysGagnant=='Fr' :
    CôteGagnant=CoteFr
elif PaysGagnant=='NUL' or PaysGagnant=='nul' or PaysGagnant=='Nul':
    CôteGagnant=CoteNul
else:
    CôteGagnant=CoteAu

if Gagnant==0 and ScoreExact==0:
    Total=0
if Gagnant==1 and ScoreExact==0:
    Total=Mise*CôteGagnant
if Gagnant==0 and ScoreExact==1:
    Total=Mise*3
    print("Tricheur")
if Gagnant==1 and ScoreExact==1:
    Total=Mise*CôteGagnant + Mise*3

Benef=Total-Mise
print("Bénefice de :", Benef)