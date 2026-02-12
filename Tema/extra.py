# Se dau urmatoarele expresii matematice:
# ((a + b) * (c - d) + e) / f - (g * (h + i)) -> corect deschise si inchise
# ((a + b) * (c - d) + e) / f - )g * (h + i)( -> incorect deschise si inchise
# Sa se verifice daca parantezele sunt corect deschise si inchise.
def verifica_paranteze(expresie):
    stiva = []
    for char in expresie:
        if char == '(':
            stiva.append(char)
        elif char == ')':
            if not stiva:
                return False
            stiva.pop()
    return len(stiva) == 0


expresie1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
expresie2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("
print(verifica_paranteze(expresie1))
print(verifica_paranteze(expresie2))
# Soluție alternativă fără funcție
expresie1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
expresie2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("
stiva = []
for char in expresie1:
    if char == '(':
        stiva.append(char)
    elif char == ')':
        if not stiva:
            print(False)
            break
        stiva.pop()
else:
    print(len(stiva) == 0)
stiva = []
for char in expresie2:
    if char == '(':
        stiva.append(char)
    elif char == ')':
        if not stiva:
            print(False)
            break
        stiva.pop()
else:
    print(len(stiva) == 0)

expresie1 = "((a + b) * (c - d) + e / f - (g * (h + i))"
expresie2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("
lista1 = []
lista2 = []
for char in expresie1:
    if char == '(':
        lista1.append(char)
    elif char == ')':
        if not lista1:
            print(False)
            break
        lista1.pop()
else:
    print(len(lista1) == 0)
for char in expresie2:
    if char == '(':
        lista2.append(char)
    elif char == ')':
        if not lista2:
            print(False)
            break
        lista2.pop()
else:
    print(len(lista2) == 0)
