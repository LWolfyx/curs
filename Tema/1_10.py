# Încălzire (1-10):
# 1. Creează două variabile cu valori numerice și afișează suma lor.
# 2. Afișează produsul a două numere introduse de la tastatură.
# 3. Primește un nume de la tastatură și afișează-l cu litere mari.
# 4. Afișează lungimea unui string introdus de la tastatură.
# 5. Verifică dacă un număr este par sau impar.
# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.
# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.
# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.
# 9. Afișează toate caracterele unui string, câte unul pe linie.
# 10. Primește două numere și afișează cel mai mare dintre ele.

# 1
primul_numar = 5
al_doilea_numar = 10
print(primul_numar + al_doilea_numar)

# 2
var3 = int(input("Introdu numar1: "))
var4 = int(input("Introdu numar2: "))
print(var3 * var4)

# 3
nume = input("Nume: ")
print(nume.upper())

# 4
sentence = input("Introdu un string: ")
lungime_sentence = len(sentence)
print(lungime_sentence)

# 5
numar1 = int(input("Numar: "))

if numar1 % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

# 6
text = input("Text: ")
print(text.count("a"))

# 7
text2 = input("text: ")
print(text2[::-1])

# 8
numar2 = int(input("Verificare numar: "))
if numar2 > 0:
    print("Numarul este pozitiv")
elif numar2 < 0:
    print("Numarul este negativ")
else:
    print("Numarul este 0")

# 9
text3 = input("Textul: ")
for caracter in text3:
    print(caracter)

# 10
var1 = int(input("var1: "))
var2 = int(input("var2: "))
if var1 > var2:
    print(f"Numarul mai mare este {var1}")
else:
    print(f"Numarul mai mare este {var2}")
