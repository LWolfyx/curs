# 11.
var1 = int(input("Introduce numar1: "))
var2 = int(input("Introduce numar2: "))
var3 = int(input("Introduce numar3: "))

if var1 < var2 and var1 < var3:
    print(f"Cel mai mic numar este {var1}")
elif var2 < var1 and var2 < var3:
    print(f"Cel mai mic numar este {var2}")
else:
    print(f"Cel mai mic numar este {var3}")

# 13.
parola = input("Parola: ")
if len(parola) >= 8:
    has_digit = False
    for caracter in parola:
        if caracter.isdigit():
            has_digit = True
            break
    if has_digit:
        print("Parola este valida")
    else:
        print("Parola nu este valida")

# 24.
numar_adunare = input("Numar pentru adunarea lor: ")
cifre = [int(cifra) for cifra in numar_adunare]
suma = 0
for cifra in cifre:
    suma += cifra
print(f"Suma cifrelor este {suma}")

# 27
distincte = input("Text pentru distincte: ")
caractere_distincte = ""
for caracter in distincte:
    if caracter not in caractere_distincte:
        caractere_distincte += caracter
print("Caracterele distincte sunt", caractere_distincte)

# 28
aceeasi_litere = input("Text pentru aceeasi litera: ")
litere_repetate = ""
for repetate in aceeasi_litere:
    if aceeasi_litere.count(repetate) == 2 and repetate not in litere_repetate:
        litere_repetate += repetate
print("Literele repetate sunt", litere_repetate)

# 30
Verificare = input("Verificare pentru cifre, litere mari si mici: ")
L_mari = False
l_mici = False
Numere = False
for char in Verificare:
    if char.isupper():
        L_mari = True
    elif char.islower():
        l_mici = True
    elif char.isdigit():
        Numere = True
if L_mari and l_mici and Numere:
    print("Textul este valid")
else:
    print("Textul nu este valid")

# 33.
numere_text = input("Numere: ")
numere_str = numere_text.split(",")
numere = []
