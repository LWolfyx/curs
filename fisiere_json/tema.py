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

# 5
# 5.Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:
# school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
# school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info
#  Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
# Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 9.0 la Istorie
# Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80
# Calculeaza media generala a tuturor claselor de Filologie
# Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa
# Afiseaza elevii cu cea mai mare medie din fiecare clasa
# Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
# Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv.
import csv
import json
import os


def ia_media(element):
    return element[1]


def cale():
    cale_baza = os.path.dirname(os.path.abspath(__file__))
    print(f"--- Incep cautarea in: {cale_baza} ---")

    lista_medii_filo = []
    lista_clase_mate_info = []
    fisiere_gasite = False

    for root, dirs, files in os.walk(cale_baza):
        nume_director = os.path.basename(root)

        for file in files:
            fisiere_gasite = True
            cale_fisier = os.path.join(root, file)

            # FILOLOGIE
            if nume_director == "ClassA" and file.endswith(".csv"):
                print(f"Procesez CSV: {file}")
                with open(cale_fisier, mode='r', encoding='utf-8') as f:
                    reader = list(csv.DictReader(f))
                    if not reader:
                        print(f"Atentie: Fisierul {file} este gol!")
                        continue

                    suma_note_clasa = 0
                    elev_premiant = None
                    for row in reader:
                        media_generala = float(row.get('Media_Generala', 0))
                        nota_istorie = float(row.get('Istorie', 0))
                        if nota_istorie > 9.0:
                            print(
                                f"  [Filo] Istorie > 9: {row.get('Nume')} din {file}")
                        suma_note_clasa += media_generala
                        if not elev_premiant or media_generala > float(elev_premiant.get('Media_Generala', 0)):
                            elev_premiant = row

                    medie_clasa = suma_note_clasa / len(reader)
                    lista_medii_filo.append(medie_clasa)
                    print(f"  Top elev {file}: {elev_premiant['Nume']}")

            # MATE-INFO
            elif nume_director == "ClasaB" and file.endswith(".json"):
                print(f"Procesez JSON: {file}")
                with open(cale_fisier, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        if not data:
                            continue

                        suma_note_clasa = 0
                        elev_premiant = None
                        for student in data:
                            media_generala = float(
                                student.get('Media_Generala', 0))
                            if media_generala < 8.0:
                                print(
                                    f"  [Mate-Info] Medie < 8.0: {student.get('Nume')} din {file}")
                            suma_note_clasa += media_generala
                            if not elev_premiant or media_generala > float(elev_premiant.get('Media_Generala', 0)):
                                elev_premiant = student

                        medie_clasa = suma_note_clasa / len(data)
                        lista_clase_mate_info.append((file, medie_clasa))
                        print(f"  Top elev {file}: {elev_premiant['Nume']}")
                    except Exception as e:
                        print(f"Eroare la citirea JSON {file}: {e}")

    if not fisiere_gasite:
        print(
            "EROARE: Nu am gasit niciun fisier .csv sau .json in folderele ClassA/ClasaB.")

    if lista_clase_mate_info:
        print("\n--- Sortare Mate-Info ---")
        clase_sortate = sorted(lista_clase_mate_info, key=ia_media)
        for clasa, medie in clase_sortate:
            print(f" - {clasa}: {medie:.2f}")


def csv_to_json(source_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(source_folder):
        if file_name.endswith('.csv'):
            csv_path = os.path.join(source_folder, file_name)
            json_path = os.path.join(
                output_folder, file_name.replace('.csv', '.json'))

            with open(csv_path, 'r', encoding='utf-8') as f:
                # DictReader automatically uses the header row as keys
                data = list(csv.DictReader(f))

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Converted {file_name} to JSON")


# Usage
csv_to_json('ClasaA', 'ClasaA_JSON')


def json_to_csv(source_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(source_folder):
        if file_name.endswith('.json'):
            json_path = os.path.join(source_folder, file_name)
            csv_path = os.path.join(
                output_folder, file_name.replace('.json', '.csv'))

            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if data:  # Ensure file isn't empty
                # Use keys from the first dictionary as headers
                headers = data[0].keys()

                with open(csv_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(data)
                print(f"Converted {file_name} to CSV")


# Usage
json_to_csv('ClasaB', 'ClasaB_CSV')


if __name__ == "__main__":
    cale()
