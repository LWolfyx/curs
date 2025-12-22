# 11. Primește trei numere și afișează cel mai mic dintre ele.
# 12. Primește un text și verifică dacă este palindrom.
# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.
# 14. Primește un text și construiește un nou string numai cu vocalele din el.
# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).
# 16. Primește un text și afișează doar literele mici din el.
# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.
# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.
# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).
# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.
# 21. Primește un text și afișează-l inversat.
# 22. Primește o propoziție și numără câte cuvinte conține.
# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".
# 24. Primește un număr și afișează suma cifrelor sale.
# 25. Primește un text și afișează doar caracterele care sunt cifre.
# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.
# 27. Primește un text și afișează toate caracterele distincte din el.
# 28. Primește un text și afișează literele care apar de exact două ori.
# 29. Primește un număr n și afișează toți divizorii săi.
# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

# 11
var1 = int(input("Introduce numar1: "))
var2 = int(input("Introduce numar2: "))
var3 = int(input("Introduce numar3: "))
print(min(var1, var2, var3))

# 12
palindrom = input("Verificare palindrom: ")
if palindrom == palindrom[::-1]:
    print("Este palindrom")
else:
    print("Nu este palindrom")

# 13
parola = input("Parola: ")
if len(parola) >= 8 and any(caracter.isdigit() for caracter in parola):
    print("Parola este valida")
else:
    print("Parola nu este valida")

# 14
text = input("Text cu vocale: ")
vocale = "aeiouAEIOU"
text_vocale = "".join([car for car in text if car in vocale])
print("Textul format din vocale este", text_vocale)

# 15
variabila = int(input("Un numar: "))
print(f"numerele pare de la 0 la {variabila} sunt")
for i in range(0, variabila + 1, 2):
    print(i)

# 16
text2 = input("Text pentru literele mici din text: ")
litere_mici = "".join(caract for caract in text2 if caract.islower())
print("Literele mici din text sunt", litere_mici)

# 17
numar = int(input("Primul numar: "))
numar2 = int(input("Al doilea numar: "))
for i in range(min(numar, numar2), max(numar, numar2)+1):
    print(i)

# 18
text3 = input("Text: ")
cuvinte = text3.split()
for cuvant in cuvinte:
    print(cuvant)

# 19
numar_produs = int(input("Numar pt inmultire: "))
print(f"Tabla inmultirii pentru acest {numar_produs} este: ")
for i in range(1, 11):
    print(f"{numar_produs} * {i} = {numar_produs * i}")

# 20
text4 = input("Orice tip de text pentru verificare litere mici: ")
if text4.islower():
    print("Toate literele sunt mici")
else:
    print("Nu toate literele sunt mici")

# 21
text5 = input("Text pentru inversare: ")
print(text5[::-1])

# 22
propozitie = input("Propozitie: ")
cuvinte_propozitie = propozitie.split()
print(len(cuvinte_propozitie), "acesta este numarul de cuvinte")

# 23
text_cu_spatii = input("Text cu underline: ")
text_fara_spatii = text_cu_spatii.replace("_", " ")
print(text_fara_spatii)

# 24

numar_adunare = input("Numar pentru adunarea lor: ")
suma_cifra = sum(int(cifra) for cifra in numar_adunare)
print("Suma cifrelor este", suma_cifra)

# 25

text_cifre = input("Text cu cifre: ")
caractere_cifre = "".join(cifre for cifre in text_cifre if cifre.isdigit())
print(caractere_cifre, "acestea sunt cifrele din text")

# 26
same = input("Text cu aceeasi litera: ")
if same[0].lower() == same[-1].lower():
    print("Sunt cu aceeasi litera")
else:
    print("Nu sunt cu aceeasi litera")

# 27
distincte = input("Text pentru distincte: ")
caractere_distincte = set(distincte)
print("Caracterele distincte sunt", caractere_distincte)

# 28
aceeasi_litere = input("Text pentru aceeasi litera: ")
litere_repetate = "".join(repetate for repetate in set(
    aceeasi_litere) if aceeasi_litere.count(repetate) == 2)
print("Literele repetate sunt", litere_repetate)

# 29
n = int(input("Numar pentru n: "))
print(f"Divizorii pentru {n} sunt:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# 30
Verificare = input("Verificare pentru cifre, litere mari si mici: ")
L_mari = any(char.isupper() for char in Verificare)
l_mici = any(char.islower() for char in Verificare)
Cifre = any(char.isdigit() for char in Verificare)
if L_mari and l_mici and Cifre:
    print("Textul are cel putin una din toate 3")
else:
    print("Textul nu are cel putin una din cele 3")
