#PROBLEME 1 : ANALYSE ET TRANSFORMATION 

phrase=input("Saisir une phrase : ")
phrase2=input ("Entrer une nouvelle phrase :")

minuscule=phrase.casefold()
decoupage=phrase.split()

print(f"le nombre de total de mots est {len(decoupage)}")
mot_long=max(decoupage , key=len)
print(f"le mot le plus long est {mot_long}")

voyelle="a,i,o,e,u,y,A,I,O,U,Y,E"
cpt=0
for i in range (len(phrase)):
    if(phrase[i] in voyelle):
        cpt+=1
print(f"le nombre total de voyelle dans la phrase est {cpt}")

def transformationmotpaire(phrase):
    mots=phrase.split()
    resultat = []
    for mot in mots:
        if (len(mot)) %2 == 0:
            resultat.append(mot.upper())
        else:
            resultat.append(mot.lower())
        return "".join(resultat)

resultat_final=transformationmotpaire(phrase2)
print(resultat_final)




