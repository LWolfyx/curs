import csv
import json
import os

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
