# Exercitii pentru tuples:
# 1) Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran.
#     Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

# Se da tuplul: fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi').

# 2) Afișează al doilea și al patrulea fruct din tuplu.

# 3) Afișează tuplul inversat.

# 4) Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător.

# 5) Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original.

# 6) Afișează lungimea fiecarui element din tuplu.

# 7) Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul.

# 8) Adauga un fruct nou 'ananas' in tuplu.

# 9) Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate
#    si afisati-le.

# 1
# fructe = ('măr', 'banană', 'cireașă')
# print(fructe[0], fructe[1], fructe[2])

# 2
# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print(fructe[1], fructe[3])

# 3
# print(fructe[::-1])

# 4
# if 'kiwi' in fructe:
#     print("Kiwi este în tuplu.")
# else:
#     print("Kiwi nu este în tuplu.")

# # 5
# tuplu_pare = tuple(fructe[i] for i in range(len(fructe)) if i % 2 == 0)
# print(tuplu_pare)

# # 6
# for fruct in fructe:
#     print(f"{fruct}: {len(fruct)}")

# # 7
# alt_tuplu = ('ananas', 'mango')
# tuplu_concatenat = fructe + alt_tuplu
# print(tuplu_concatenat)

# # 8
# fructe_list = list(fructe)
# fructe_list.append('ananas')
# fructe = tuple(fructe_list)
# print(fructe)

# # 9
# fructe = ('măr', 'banană', 'cireașă')
# a, b, c = fructe
# print(a)
# print(b)
# print(c)


# Exerciții pentru seturi:
# 1) Creează un set care conține numele a cinci culori și afișează-le pe ecran.

# 2) Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

# 3) Elimină o culoare din set și afișează setul actualizat.

# 4) Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător.

# 5) Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

# 6) Afișează toate culorile din primul set care nu sunt în al doilea set.

# 7) Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista, astfel incat fiecare element sa apara o singura data.

# 1
culori = {'roșu', 'verde', 'albastru', 'galben', 'portocaliu'}
print(culori)

# 2
culori.add('mov')
print(culori)

# 3
culori.remove('verde')
print(culori)

# 4
if 'albastru' in culori:
    print("Albastru este în set.")
else:
    print("Albastru nu este în set.")

# 5
alt_set = {'negru', 'alb', 'roșu'}
culori_comune = culori.intersection(alt_set)
print(culori_comune)

# 6
culori_diferite = culori.difference(alt_set)
print(culori_diferite)

# 7
lista = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
set_fara_duplicate = set(lista)
print(set_fara_duplicate)
lista_fara_duplicate = list(set_fara_duplicate)
print(lista_fara_duplicate)
