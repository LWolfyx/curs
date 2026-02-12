# Exercitii Functii recursive:
# 1) Scrie o funcție recursivă care calculează factorialul unui număr.
# Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120
# 2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
# Ex: pentru n=5, returnează 15 (1+2+3+4+5)
# 3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
# Ex: pentru 1234 returneaza 4
# 4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3
# 5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
# Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28

# 1) Scrie o funcție recursivă care calculează factorialul unui număr.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("n = "))
print(factorial(n))
# 2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.


def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n - 1)


n = int(input("n = "))
print(suma(n))
# 3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.


def numar_cifre(n):
    if n < 10:
        return 1
    else:
        return 1 + numar_cifre(n // 10)


n = int(input("n = "))
print(numar_cifre(n))

# 4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.


def adancime_lista(lst):
    if not isinstance(lst, list):
        return 0
    else:
        return 1 + max(adancime_lista(item) for item in lst)


lst = [1, 2, [3, 4, [5, 6]], 7]
print(adancime_lista(lst))
# 5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.


def suma_lista(lst):
    if not isinstance(lst, list):
        return lst
    else:
        return sum(suma_lista(item) for item in lst)


lst = [1, 2, [3, 4, [5, 6]], 7]
print(suma_lista(lst))

# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

print(
    """
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

"""
)

elevi = [{'nume': 'popescu', 'prenume': 'ana', 'nota romana': 6.0, 'nota mate': 7.0, 'nota engleza': 8.0, 'media': 7.0}, 
         {'nume': 'abesei', 'prenume': 'paul', 'nota romana': 7.0, 'nota mate': 8.0, 'nota engleza': 9.0, 'media': 8.0},
         {'nume': 'popescu', 'prenume': 'andrei', 'nota romana': 3.0, 'nota mate': 4.0, 'nota engleza': 5.0, 'media': 4.0}
         ]

def adauga_elev ():
    nume = input("Nume : ")
    prenume = input("Prenume : ")
    nota_romana = float(input("Nota romana :"))
    nota_mate = float(input("Nota mate :"))
    nota_engl = float(input("Nota engleza :"))
    elev = {
        "nume": nume,
        "prenume": prenume,
        "nota romana" : nota_romana,
        "nota mate" : nota_mate,
        "nota engleza" : nota_engl,
        "media" : calculeaza_media(nota_romana, nota_mate, nota_engl)
    }
    elevi.append(elev)

def calculeaza_media(nota_romana, nota_mate, nota_engl):
    x = round((nota_romana + nota_mate + nota_engl)/3,2)
    return x

def ia_media(elev):
    return elev['media']

def ia_nume(elev):
    return elev['nume']

def afiseaza_elevi():
    for elev in elevi :
        print(f"{elev['nume']} {elev['prenume']} | "
            f"Romana: {elev['nota romana']} | "
            f"Matematica: {elev['nota mate']} | "
            f"Engleza: {elev['nota engleza']} | "
            f"Media: {elev['media']}")
        
def afisare_alfabetic():
    elevi_sortati = sorted(elevi, key=ia_nume)
    for elev in elevi_sortati:
        print(f"{elev['nume']} {elev['prenume']}")
        
def sterge_elevi():
    nume = input("Ce nume vrei elimini ? ")
    prenume = input("Ce prenume vrei sa elimini ?")
    for elev in elevi :
        if elev["nume"] == nume and elev["prenume"] == prenume:
            elevi.remove(elev)
            print("Am sters")
            return
    print("Elevul nu a fost gasit")

def modificare ():
    nume = input("Ce nume sa modific : ")
    prenume = input("Ce prenume sa modific : ")
    for elev in elevi: 
        if elev['nume'] == nume and elev['prenume'] == prenume:
            elev['nota romana'] = float(input("Nota roamana noua: "))
            elev['nota mate'] = float(input("Nota mate noua: "))
            elev['nota engleza'] = float(input("Nota engleza noua: "))
            elev['media'] = calculeaza_media(elev['nota romana'], elev['nota mate'], elev['nota engleza'])
            print("Date modificate success!")
            return
    print("Elev negasit!")

def cauta_elevi():
    nume = input("Ce nume vrei ? ")
    prenume = input("Ce prenume vrei ?")
    for elev in elevi :
        if elev["nume"] == nume and elev["prenume"] == prenume:
            print(f"{elev['nume']} {elev['prenume']} | "
            f"Romana: {elev['nota romana']} | "
            f"Matematica: {elev['nota mate']} | "
            f"Engleza: {elev['nota engleza']} | "
            f"Media: {elev['media']}")
            return
    print("Elevul nu a fost gasit")

def afiseaza_media_crescator():
    elevi_sortati = sorted(elevi, key=ia_media)
    for elev in elevi_sortati:
        print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")

def medie_5 ():
    for elev in elevi :
        if elev['media'] >= 5:
            print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")
            
while True :
    optiune = input("Alege optiune : ")
    if optiune == '0' :
        print("Ai iesit din sistem")
        break
    if optiune == "1" :
        adauga_elev()
    if optiune == "2" :
        afiseaza_elevi()
    if optiune == "3" :
        modificare()
    if optiune == "4":
        sterge_elevi()
    if optiune == "5":
        cauta_elevi()
    if optiune == "6":
        afiseaza_media_crescator()
    if optiune == "7":
        medie_5()
    if optiune == "8":
        afisare_alfabetic()