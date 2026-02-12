# Exercitii pentru dictionare:
# 1) Creeaza un dictionar care sa contina numele si varsta a 5 persoane.
# 2) Afiseaza varsta unei persoane specifificate de utilizator.
# 3) Afiseaza cea mai mare si cea mai mica varsta din dictionar.
# 4) Adauga 3 noi persoane in dictionar.
# 5) Afiseaza varsta medie a persoanelor din dictionar.
# 6) Sterge o persoana specificata de utilizator din dictionar.
# 7) Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.
# 8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".
# 9) Verifica daca o persoana specificata de utilizator exista in dictionar.
# 10) Actualizeaza varsta unei persoane specificate de utilizator.
# 11) Afiseaza numarul total de persoane din dictionar.
# 12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.
# 13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.
# 14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.
# 15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.
# 16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).
# 17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).
# 18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
#    (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).
# 19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
# 20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.

# 1) Creeaza un dictionar care sa contina numele si varsta a 5 persoane
# dictionar_persoane = {"Ana": 25, "Ion": 30,
#                       "Maria": 22, "George": 28, "Elena": 27}
# print(dictionar_persoane)
# 2) Afiseaza varsta unei persoane specifificate de utilizator
# nume = input("Introdu numele persoanei: ")
# if nume in dictionar_persoane:
#     print(f"Varsta lui {nume} este {dictionar_persoane[nume]}")

# 3) Afiseaza cea mai mare si cea mai mica varsta din dictionar
# varste = dictionar_persoane.values()
# print(f"Cea mai mica varsta este {min(varste)}")
# print(f"Cea mai mare varsta este {max(varste)}")
# 4) Adauga 3 noi persoane in dictionar
# dictionar_persoane["Vasile"] = 35
# dictionar_persoane["Cristina"] = 29
# dictionar_persoane["Mihai"] = 31
# print(dictionar_persoane)
# 5) Afiseaza varsta medie a persoanelor din dictionar
# media_varste = sum(dictionar_persoane.values()) / len(dictionar_persoane)
# print(f"Varsta medie este {media_varste}")
# 6) Sterge o persoana specificata de utilizator din dictionar
# nume_sters = input("Introdu numele persoanei de sters: ")
# if nume_sters in dictionar_persoane:
#     del dictionar_persoane[nume_sters]
#     print(f"{nume_sters} a fost sters din dictionar.")
# print(dictionar_persoane)
# 7) Afiseaza toate persoanele cu varsta peste o valoare specificata
# valoare = int(input("Introdu o valoare pentru varsta: "))
# for nume, varsta in dictionar_persoane.items():
#     if varsta > valoare:
#         print(f"{nume}: {varsta}")
# 8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>"
# for nume, varsta in dictionar_persoane.items():
#     print(f"Nume: {nume}, Varsta: {varsta}")
# 9) Verifica daca o persoana specificata de utilizator exista in dictionar
# nume_cautat = input("Introdu numele persoanei de cautat: ")
# if nume_cautat in dictionar_persoane:
#     print(f"{nume_cautat} exista in dictionar.")
# else:
#     print(f"{nume_cautat} nu exista in dictionar.")
# 10) Actualizeaza varsta unei persoane specificate de utilizator
# nume_actualizat = input("Introdu numele persoanei de actualizat: ")
# if nume_actualizat in dictionar_persoane:
#     varsta_noua = int(input("Introdu noua varsta: "))
#     dictionar_persoane[nume_actualizat] = varsta_noua
#     print(f"Varsta lui {nume_actualizat} a fost actualizata la {varsta_noua}.")
# print(dictionar_persoane)
# 11) Afiseaza numarul total de persoane din dictionar
# print(f"Numarul total de persoane este {len(dictionar_persoane)}")
# 12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le
# lista_nume = list(dictionar_persoane.keys())
# print(lista_nume)
# 13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani
# dictionar_adulti = {nume: varsta for nume, varsta in dictionar_persoane.items() if varsta > 18}
# print(dictionar_adulti)
# 14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o
# lista_varste_fara_duplicate = list(set(dictionar_persoane.values()))
# print(lista_varste_fara_duplicate)
# 15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator
# valoare_apropiata = int(input("Introdu o valoare pentru a gasi varsta apropiata: "))
# cel_mai_apropiat_nume = None
# cel_mai_apropiat_varsta = None
# min_diferenta = float('inf')
# for nume, varsta in dictionar_persoane.items():
#     diferenta = abs(varsta - valoare_apropiata)
#     if diferenta < min_diferenta:
#         min_diferenta = diferenta
#         cel_mai_apropiat_nume = nume
#         cel_mai_apropiat_varsta = varsta
# print(f"Persoana cu varsta cea mai apropiata de {valoare_apropiata} este {cel_mai_apropiat_nume} cu varsta {cel_mai_apropiat_varsta}.")
# 16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.)
# decade = {}
# for nume, varsta in dictionar_persoane.items():
#     decade_key = (varsta // 10) * 10
#     if decade_key not in decade:
#         decade[decade_key] = []
#     decade[decade_key].append(nume)
# for decade_key, persoane in decade.items():
#     print(f"{decade_key}-{decade_key + 9}: {', '.join(persoane)}")
# 17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).
# persoane_sortate_alfabetic = dict(sorted(dictionar_persoane.items()))
# print(persoane_sortate_alfabetic)
# 18) Afiseaza persoanele sortate dupa varsta, de la cea mai
# mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
# persoane_sortate_dupa_varsta = dict(sorted(dictionar_persoane.items(), key=lambda item: item[1]))
# print(persoane_sortate_dupa_varsta)
# 19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"
dictionar_persoane_text = {}
parti = text.split(", ")
for parte in parti:
    cuvinte = parte.split(" ")
    nume = cuvinte[0]
    varsta = int(cuvinte[2])
    dictionar_persoane_text[nume] = varsta
print(dictionar_persoane_text)
# 20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#     Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.
text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"
frecventa_litere = {}
for char in text:
    if char.isalpha():
        char_lower = char.lower()
        if char_lower in frecventa_litere:
            frecventa_litere[char_lower] += 1
        else:
            frecventa_litere[char_lower] = 1
print(frecventa_litere)
