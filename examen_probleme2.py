#PROBLEME 2 :GESTION DES NOTES D'UNE CLASSE 

Students = [
    ("Ali", 12),
    ("Fatou",17),
    ("Moussa",9),
    ("Awa",14),
    ("Ibrahima",7)
]

print(Students)
def moyenne(liste):
    if not liste:
        print("la liste est vide")
        return
    somme = sum(note for (_, note) in liste)
    moyenne = somme / len(liste)
    print(f"la moyenne de la classe est de : {moyenne:.2f}")
    return moyenne

def note_max(liste):
    name, note = max(liste, key=lambda student: student[1])
    print(f"la note maximale est de {note} obtenue par {name}")
    return name, note

def note_min(liste):
    name, note = min(liste, key=lambda student: student[1])
    print(f"la note minimale est de {note} obtenue par {name}")
    return name, note


def affichage_admis(liste):
    print("les etudiants admis d'office sont :")
    for name, note in liste:
        if note >= 10:
            print(f" {name} : {note}")


def affichage_ajournes(liste):
    print("les etudiants ajournes d'office sont :")
    for name, note in liste:
        if note < 10:
            print(f" {name} : {note}")


def noms_admis_trie(liste):
    noms = [name for name, note in liste if note >= 10]
    noms.sort()
    return noms


