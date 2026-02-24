'''
Exercitii JSON si CSV:
1.Sa se scrie un program care citeste de la tastatura informatii desre persone (nume, prenume, varsta, oras)
pana la introducerea cuvantului "exit" si le salveaza intr-un fisier JSON numit "persoana.json".
2.Sa se scrie un program care citeste date despre produse (nume, pret, cantitate) de la tastatura pana la introducerea cuvantului "exit" si le salveaza intr-un fisier CSV numit "produse.csv".
3.Sa se scrie un program care citeste datele despre produse din fisierul "produse.csv", adauga un camp nou "pret_total" care reprezinta pretul total al stocului pentru fiecare produs (pret * cantitate) si salveaza datele intr-un fisier "produse.json".
4.Sa se scrie un program care citeste datele despre produse din fisierul "produse.json", adauga un camp nou "tara_origine" care reprezinta tara de origine a produsului si salveaza datele intr-un fisier "produse.csv".
'''
'''
5.Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:
school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info 
 Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80
Calculeaza media generala a tuturor claselor de Filologie
Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa
Afiseaza elevii cu cea mai mare medie din fiecare clasa
Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv.
'''

# #1


# import json


# persoane = []

# while True:
#     nume = input("Introduceti numele (sau 'exit' pentru a opri): ")
#     if nume.lower() == "exit":
#         break
#     prenume = input("Introduceti prenumele: ")
#     varsta = int(input("Introduceti varsta: "))
#     oras = input("Introduceti orasul: ")

#     persoana = {
#         "nume": nume,
#         "prenume": prenume,
#         "varsta": varsta,
#         "oras": oras
#     }

#     persoane.append(persoana)

# with open("persoane.json", "w") as f:
#     json.dump(persoane, f, indent=4)


# #2
# import csv
# produse = []
# while True:
#     nume = input("Introduceti numele produsului (sau 'exit' pentru a opri): ")
#     if nume.lower() == "exit":
#         break
#     pret = float(input("Introduceti pretul: "))
#     cantitate = int(input("Introduceti cantitatea: "))

#     produs = {
#         "nume": nume,
#         "pret": pret,
#         "cantitate": cantitate
#     }

#     produse.append(produs)
# with open("produse.csv", "w", newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=["nume", "pret", "cantitate"])
#     writer.writeheader()
#     writer.writerows(produse)

# #3
# import json
# import csv
# produse = []
# with open("produse.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         row["pret"] = float(row["pret"])
#         row["cantitate"] = int(row["cantitate"])
#         row["pret_total"] = row["pret"] * row["cantitate"]
#         produse.append(row)
# with open("produse.json", "w") as f:
#     json.dump(produse, f, indent=4)
# #4
# import json
# import csv
# produse = []
# with open("produse.json", "r") as f:
#     produse = json.load(f)
# for produs in produse:
#     produs["tara_origine"] = input(f"Introduceti tara de origine pentru {produs['nume']}: ")
# with open("produse.csv", "w", newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=["nume", "pret", "cantitate", "pret_total", "tara_origine"])
#     writer.writeheader()
#     writer.writerows(produse)


import os
import csv
import json

clasaA = 'fisiere_json/ClassA'

# for file_name in os.listdir(clasaA):
#     cale_fisier = os.path.join(clasaA, file_name)

#     with open(cale_fisier, 'r', newline="") as my_file:
#         reader = csv.DictReader(my_file)
#         for row in reader:
#             if int(row["Istorie"]) >= 90:
#                 print(row)

clasaB = 'fisiere_json/ClasaB'
# for file_name in os.listdir(clasaB):
#     cale_fisier = os.path.join(clasaB, file_name)

#     with open(cale_fisier, 'r', encoding='utf-8') as my_file:
#         date = json.load(my_file)
#         for student in date:

#             media_generala = float(
#                 student['Istorie'] + student['Informatica'] + student['Romana'])/3
#             if media_generala < 80:
#                 print(
#                     f"  [Mate-Info] Medie < 80: {student.get('Nume')} are media {media_generala}")

for file_name in os.listdir(clasaA):
    path_files = os.path.join(clasaA, file_name)
    with open(path_files, 'r', newline='') as my_file:
        reader = csv.DictReader(my_file)
        toate_mediile_elevilor = []
        for row in reader:
            medie_elev = (int(row["Geography"]) +
                          int(row["English"]) + int(row["Istorie"]))/3
        toate_mediile_elevilor.append(medie_elev)
        medie_clasei = sum(toate_mediile_elevilor) / \
            len(toate_mediile_elevilor)
        print(f"{path_files} are medie {medie_clasei}")
