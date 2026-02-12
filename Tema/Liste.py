"""
1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
Exemplu: 10, 50 -> 16, 32

3) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

5) Afișează toate elementele de pe poziții impare dintr-o listă dată.
Exemplu: [10,20,30,40,50,60] -> 20,40,60

6) Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]

7) Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

8) Elimină toate elementele pare dintr-o listă de numere.
Exemplu: [1,2,3,4,5,6] -> [1,3,5]

9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False

11) Interclasează două liste de aceeași lungime într-o singură listă.
# Exemplu: [1,2], [3,4] => [1,3,2,4]

12) Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

13) Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
Fara a folosi set().
# Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

14) Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

15) Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
Fara a folosi functia sort() sau sorted().
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

16) Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

Pentru generarea numarului aleator:
import random
numar_aleator = random.randint(1, 100)

21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
in functie de numele de familie.
"""
# 1) Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator. Exemplu: 10, 50 -> 16, 32
# valoare1 = int(input("Introduce prima valoare a intervalului: "))
# valoare2 = int(input("Introduce a doua valoare a intervalului: "))

# putere = 1

# while putere < valoare2:
#     putere *= 2
#     if valoare1 < putere < valoare2:
#         print(putere)

# 3) Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg(). Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# lista = (input("Introduce lista cu 7 valori: ")).split()
# numbers = [int(n) for n in lista]
# suma = 0

# for n in numbers:
#     print(n)
#     suma += n
#     medie = suma/len(numbers)
# print(medie, suma)

# 4) Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată. Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]
# lista = input("Introduce o lista: ").split()
# print(lista)
# elemente = lista[::-1]
# print(elemente)

# 5) Afișează toate elementele de pe poziții impare dintr-o listă dată. Exemplu: [10,20,30,40,50,60] -> 20,40,60
# lista = input("Whatever: ").split()
# numere = [int(n) for n in lista]
# for i in range(1, len(numere), 2):
#     if i % 2 != 0:
#         print(numere[i])

# 6) Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]
# lista = input("Lista: ").split()
# numere = [int(n) for n in lista]
# element_vechi = int(input("Elementul de inlocuit: "))
# element_nou = int(input("Elementul nou: "))

# for i in range(len(numere)):
#     if numere[i] == element_vechi:
#         numere[i] = element_nou

# print(numere)

# 7) Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1
# lista = input("Lista: ").split()
# numere = [int(n) for n in lista]
# maxim = numere[0]
# minim = numere[0]

# for n in numere:
#     if n > maxim:
#         maxim = n
#     if n < minim:
#         minim = n
# print(f"Maxim: {maxim}, Minim: {minim}")

# 8) Elimină toate elementele pare dintr-o listă de numere. Exemplu: [1,2,3,4,5,6] -> [1,3,5]
# lista = input("Lista: ").split()
# numere = [int(n) for n in lista]
# numere_impare = []
# for n in numere:
#     if n % 2 != 0:
#         numere_impare.append(n)
# print(numere_impare)

# 9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']
# lista = input("Lista cu cuvinte care contin \"a\":").split()
# lista_a = []
# for cuvant in lista:
#     if 'a' in cuvant or 'A' in cuvant:
#         lista_a.append(cuvant)
# print(lista_a)

# 10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# lista = input("Introduce lista pentru verificare palindrom: ").split()
# if lista == lista[::-1]:
#     print("Lista este palindrom")
# else:
#     print("Nu este palindrom")

# 11) Interclasează două liste de aceeași lungime într-o singură listă.
# lista1 = input("Prima lista: ").split()
# lista2 = input("Lista sa fie de aceeasi marima ca prima: ").split()
# if len(lista1) == len(lista2):
#     lista1.extend(lista2)
#     print(lista1)
# else:
#     print("Listele nu au aceeasi marime")

# 12) Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# lista = input("Introduce lista: ").split()
# lista_index_valoare = []
# for i, valoare in enumerate(lista):
#     lista_index_valoare.append([i, valoare])
# print(lista_index_valoare)

# 13) Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice). Fara a folosi set(). Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]
# lista = input("Introduce lista: ").split()
# numere = [int(n) for n in lista]
# numere_unice = []
# for n in numere:
#     if numere.count(n) == 1:
#         numere_unice.append(n)
# print(numere_unice)
# 14) Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# lista = input("Introduce lista: ").split()
# numere = [int(n) for n in lista]
# negative = []
# pozitive_zero = []
# for n in numere:
#     if n < 0:
#         negative.append(n)
#     elif n >= 0:
#         pozitive_zero.append(n)
# print(negative)
# print(pozitive_zero)

# 15) Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string. Fara a folosi functia sort() sau sorted(). Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']
# lista = input("Whatever v2: ").split()
# vocale = "aeiouAEIOU"
# lista_sortata = []
# for cuvant in lista:
#     numar_vocale = 0
#     for caracter in cuvant:
#         if caracter in vocale:
#             numar_vocale += 1

#     lista_sortata.append((cuvant, numar_vocale))
# for i in range(len(lista_sortata)):
#     for j in range(i + 1, len(lista_sortata)):
#         if lista_sortata[i][1] > lista_sortata[j][1]:
#             lista_sortata[i], lista_sortata[j] = lista_sortata[j], lista_sortata[i]

# lista_finala = [cuvant for cuvant, _ in lista_sortata]
# print(lista_finala)

# 16) Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# matrice = input("Introduce matricea, fiecare rand separat prin ; si elementele prin spatiu: ").split(';')
# matrice = [[int(num) for num in rand.strip().split()] for rand in matrice]
# suma_diagonala = 0
# if all(len(rand) == len(matrice) for rand in matrice):
#     for i in range(len(matrice)):
#         suma_diagonala += matrice[i][i]
#     print(suma_diagonala)
# else:
#     print("Matricea nu este patrata")

# 17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.
# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
# print(lista[1][1])

# 18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.
# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
# print(lista[1][2][2])

# 19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element_cautat = int(input("Elementul de cautat: "))
# count = 0
# for elm in lista:
#      if type(elm) == int:
#         if elm== element_cautat:
#             count += 1
#     elif type(elm) == list:
#         for sub in elm:
#             if type(sub) == int:
#                 if sub == element_cautat:
#                     count += 1
#             elif type(sub) == list:
#                 for subin in sub:
#                     if type(subin) == int:
#                         if subin == element_cautat:
#                             count += 1
# print(count)

# 20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# import random
# numar_aleator = random.randint(1, 100)
# incercari = 0
# while True:
#     ghicire = input("Ghiceste numarul intre 1 si 100 (sau scrie 'exit' pentru a iesi): ")
#     if ghicire.lower() == 'exit':
#         print(f"Ai iesit din joc dupa {incercari} incercari.")
#         break
#     ghicire = int(ghicire)
#     incercari += 1
#     if ghicire < numar_aleator:
#         print("Numarul este mai mare.")
#     elif ghicire > numar_aleator:
#         print("Numarul este mai mic.")
#     else:
#         print(f" Ai ghicit numarul {numar_aleator} in {incercari} incercari.")
#         break

# 21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica in functie de numele de familie.
# date = []
# while True:
#     intrare = input("Introduce datele (sau # pentru a termina): ")
#     if intrare == '#':
#         break
#     parti = intrare.split()
#     nume = parti[0]
#     prenume = parti[1]
#     date.append((nume, prenume))
# date.sort()
# for nume, prenume in date:
#     print(f"Nume: {nume} Prenume: {prenume}")

"""==================================================================================================================================================================================== """

# Folositi list comprehension pentru a rezolva urmatoarele exercitii:
# 1) Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 2) Creeaza o lista cu toate numerele pare intre divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]
# 3) Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]
# 4) Dintr-o lista cu numere de la 1 la 25, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]
# 5) Creeaza o lista cu toate vocalele dintr-un text dat. Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']

# Folositi any pentru rezolvarea urmatoarelor exercitii:
# 1) Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True
# 2) Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True
# 3) Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True
# 4) Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True
# 5) Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True

"""===================================================================================================================================================================================="""


# 1) Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# patrate = [x**2 for x in range(10)]
# print(patrate)

# 2) Creeaza o lista cu toate numerele pare intre divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]
# lista = []
# for x in range(1, 51):
#     if x % 2 == 0 and x % 3 == 0:
#         lista.append(x)
#     else:
#         print("Numerele nu sunt pare sau divizibile cu 3")
# print(lista)

# 3) Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]
# lista = input("Whatever.v3: ").split()
# lungimi = [len(cuvant) for cuvant in lista]
# print(lungimi)

# 4) Dintr-o lista cu numere de la 1 la 25, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]
# patrate = [x**2 for x in range(1, 26) if x**2 % 4 == 0 and x**2 % 6 == 0]
# print(patrate)

# 5) Creeaza o lista cu toate vocalele dintr-un text dat. Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']
# text = input("Introduce textul: ")
# vocale = [litera for litera in text if litera in 'aeiouAEIOU']
# print(vocale)

"""===================================================================================================================================================================================="""

# 1) Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True
# lista = input("Introduce lista: ").split()
# numere = [int(n) for n in lista]
# exista_par = any(n % 2 == 0 for n in numere)
# print(exista_par)

# 2) Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True
# lista = input("Introduce lista de cuvinte: ").split()
# exista_z = any('z' in cuvant or 'Z' in cuvant for cuvant in lista)
# print(exista_z)

# 3) Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True
# lista = input("Introduce lista: ").split()
# numere = [int(n) for n in lista]
# exista_negativ = any(n < 0 for n in numere)
# print(exista_negativ)

# 4) Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True
# lista = input("Introduce lista de stringuri: ").split()
# exista_gol = any(len(sir) == 0 for sir in lista)
# print(exista_gol)

# 5) Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True
# lista = input("Introduce lista de caractere: ").split()
# exista_vocala_mare = any(litera in 'AEIOU' for litera in lista)
# print(exista_vocala_mare)
