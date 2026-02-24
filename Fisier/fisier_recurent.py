'''
Exercitii parcurgere foldere:
1.Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza numele tuturor fisierelor cu extensia ".py".
2.Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza calea absoluta a tuturor fisierelor ".txt".
3.Sa se scrie un program care parcurge recursiv un folder si scrie intr-un fisier calea absoluta catre toate fisierele gasite in folderul respectiv.
4.Sa se scrie un program care parcurge recursiv un folder si afiseaza numarul total de fisiere si directoare din acel folder.
5.Sa se scrie un program care primeste un folder si o extensie de fisier de la utilizator si parcurge recursiv folderul
pentru a afisa numele tuturor fisierelor care au acea extensie.
'''
# 1
import os


def parcurgere_folder(folder, extensie):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extensie):
                print(os.path.join(root, file))


folder = input("Introduceti calea catre folder: ")
extensie = input("Introduceti extensia fisierelor (ex: .py): ")
parcurgere_folder(folder, extensie)

# 2


def parcurgere_folder(folder, extensie):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extensie):
                print(os.path.abspath(os.path.join(root, file)))


folder = input("Introduceti calea catre folder: ")
extensie = input("Introduceti extensia fisierelor (ex: .txt): ")
parcurgere_folder(folder, extensie)

# 3


def parcurgere_folder(folder, fisier_output):
    with open(fisier_output, 'w') as f:
        for root, dirs, files in os.walk(folder):
            for file in files:
                f.write(os.path.abspath(os.path.join(root, file)) + '\n')


folder = input("Introduceti calea catre folder: ")
fisier_output = input("Introduceti numele fisierului de output: ")
parcurgere_folder(folder, fisier_output)
# 4


def parcurgere_folder(folder):
    numar_fisiere = 0
    numar_directoare = 0
    for root, dirs, files in os.walk(folder):
        numar_fisiere += len(files)
        numar_directoare += len(dirs)
    print(f"Numar total de fisiere: {numar_fisiere}")
    print(f"Numar total de directoare: {numar_directoare}")


folder = input("Introduceti calea catre folder: ")
parcurgere_folder(folder)
# 5


def parcurgere_folder(folder, extensie):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extensie):
                print(file)


folder = input("Introduceti calea catre folder: ")
extensie = input("Introduceti extensia fisierelor (ex: .txt): ")
parcurgere_folder(folder, extensie)
