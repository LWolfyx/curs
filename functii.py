# Exercitii Functii Python:
# 1) Scrie o funcție care primește un nume și afișează "Salut, <nume>!".
# 2) Scrie o funcție care primește două numere și returnează suma lor.
# 3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).
# 4) Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.
# 5) Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.
# 5) Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.
# 6) Scrie o funcție care primește un string și returnează stringul inversat.
# 7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.
# 8) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.
# 9) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.
# 10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.
# 11) Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.
# 12) Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.
# 13) Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa).
# 14) Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.
# 15) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.

# 1 Scrie o funcție care primește un nume și afișează "Salut, <nume>!".
# def salut():
#     nume = input("Nume: ")
#     return nume


# nume = salut()
# print(f"Salut, {nume}!")


# 2 Scrie o funcție care primește două numere și returnează suma lor.


# def suma():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return a + b


# print(suma())

# 3 Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).


# def calcule():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return (a + b, a - b, a * b)


# print(calcule())

# 4 Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.
# def este_par():
#     n = int(input("Numar: "))
#     return n % 2 == 0


# print(este_par())


# 5 Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.
# global_var = 0


# def patrat():
#     global global_var
#     n = int(input("Numar: "))
#     global_var = n ** 2


# patrat()
# print(global_var)

# 6  Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.
# def suma_lista():
#     lista = [int(x) for x in input("Numere: ").split("|")]
#     total = 0
#     for x in lista:
#         total += x
#     return total

# print(suma_lista())

# 7  Scrie o funcție care primește un string și returnează stringul inversat.
# def invers_string():
#     s = input("String: ")
#     return s[::-1]


# print(invers_string())

# 8 Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.
# def lungimi_stringuri():
#     lista = input("Strings: ").split()
#     return [len(s) for s in lista]

# print(lungimi_stringuri())

# 9 Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.
# def numere_comune():
#     l1 = [int(x) for x in input("List 1: ").split()]
#     l2 = [int(x) for x in input("List 2: ").split()]
#     rezultat = []

#     for x in l1:
#         if x in l2 and x not in rezultat:
#             rezultat.append(x)

#     return rezultat


# print(numere_comune())

# 10 Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.
# def cel_mai_tanar():
#     n = int(input("Cate persoane: "))
#     persoane = {}

#     for _ in range(n):
#         nume = input("Nume: ")
#         varsta = int(input("Varsta: "))
#         persoane[nume] = varsta

#     return min(persoane, key=persoane.get)

# print(cel_mai_tanar())
# 11 Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.
# def peste_18():
#     n = int(input("Cate persoane: "))
#     persoane = {}
#     rezultat = {}

#     for _ in range(n):
#         nume = input("Nume: ")
#         varsta = int(input("Varsta: "))
#         persoane[nume] = varsta

#     for nume, varsta in persoane.items():
#         if varsta > 18:
#             rezultat[nume] = varsta
#     return rezultat


# print(peste_18())


# 13 Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.
# def statistici():
#     lista = [int(x) for x in input("Numere: ").split()]
#     minim = maxim = lista[0]
#     suma = 0

#     for x in lista:
#         if x < minim:
#             minim = x
#         if x > maxim:
#             maxim = x
#         suma += x

#     return (minim, maxim, suma / len(lista))


# print(statistici())

# 14 Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa).
def frecventa():
    lista = input("Elemente: ").split()
    d = {}

    for x in lista:
        d[x] = d.get(x, 0) + 1
    return d


print(frecventa())


# 15 Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.


# def fara_duplicate():
#     lista = input("Elemente: ").split()
#     rezultat = []

#     for x in lista:
#         if x not in rezultat:
#             rezultat.append(x)

#     return rezultat


# print(fara_duplicate())

# 16 Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.


# def numere_prime():
#     lista = [int(x) for x in input("Numere: ").split()]
#     prime = []

#     for n in lista:
#         if n > 1:
#             ok = True
#             for i in range(2, int(n ** 0.5) + 1):
#                 if n % i == 0:
#                     ok = False
#                     break
#             if ok:
#                 prime.append(n)

#     return prime


# print(numere_prime())

# 12) Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.
# def mai_mici_decât_n():
#     lista = [int(x) for x in input("Numere: ").split()]
#     n = int(input("n = "))
#     rezultat = []

#     for x in lista:
#         if x < n:
#             rezultat.append(x)

#     return rezultat

# print(mai_mici_decât_n())
# 10)
# persoane = {}
# def filtru(persoane):
#     for nume, varsta in persoane.items():
#         rezultat = {}
#         if int(varsta) >= 18:
#             rezultat[nume] = varsta
#     return rezultat


# while True:
#     date = input("Introduce date: ")
#     if date == "stop":
#         break
#     alte = date.split()
#     nume = alte[2]
#     varsta = alte[-1]
#     persoane[nume] = varsta


# print(filtru(persoane))
