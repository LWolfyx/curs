'''
Exercitii lucru cu fisiere:
1. Sa se scrie un program care citeste de la tastatura informatii despre persoane (nume, prenume, varsta, oras)
   si le salveaza intr-un fisier text numit "persoana.txt" in formatul: "Nume Prenume, Varsta, Oras".

2. Sa se scrie un program care citeste un fisier text numit "date.txt" si afiseaza numarul de linii, cuvinte si caractere din fisier.

3. Se da urmatorul fisier "produse.txt" care contine informatii despre produse.
   Sa se scrie un program care citeste informatiile despre produse din fisierul "produse.txt"
   si calculeaza pretul total al stocului pentru fiecare produs.

4. Se da un fisier de logging "log.txt" care contine date referitor la evenimentele dintr-un sistem:
   Sa se scrie un program care citeste fisierul "log.txt" si afiseaza numarul de evenimente de fiecare tip (INFO, WARNING, ERROR)
   si afiseaza ora si evenimentul de tip ERROR care a avut loc cel mai recent.

5. Se da un fisier de logging "login.txt" care contine date referitor la incercarile de autentificare ale utilizatorilor:
   Sa se scrie un program care citeste fisierul "login.txt" si salveaza in fisierul "user_attempts.txt" numarul de incercari de autentificare
   pentru fiecare utilizator si ora si data ultimei incercari de autentificare reusite in formatul:
   # <user> | <numar_incercari> | <ultima_data_ora_reusita>
   '''

# 1
while True:
    raspuns = input("Mai doresti sa adaugi o persoana? (da/nu): ")

    if raspuns.lower() == "nu":
        break

    nume = input("Nume: ")
    prenume = input("Prenume: ")
    varsta = input("Varsta: ")
    oras = input("Oras: ")

    with open("persoana.txt", "a", encoding="utf-8") as f:
        f.write(f"{nume} {prenume}, {varsta}, {oras}\n")


print("Program terminat.")

# 2
file_path = "date.txt"
with open(file_path, "r", encoding="utf-8") as f:
    continut = f.read()

linii = continut.split('\n')
cuvinte = continut.split()
caractere = len(continut)

print(f"Numar de linii: {len(linii) - 1}")
print(f"Numar de cuvinte: {len(cuvinte)}")
print(f"Numar de caractere: {caractere}")

# 3
with open("produse.txt", "r", encoding="utf-8") as f:
    for linie in f:
        nume, pret, stoc = linie.strip().split("-")

        nume = nume.strip()
        pret = float(pret.strip().replace("lei", "").strip())
        stoc = int(stoc.strip().replace("bucati", "").strip())

        total = pret * stoc

        print(f"{nume} -> Total: {total} lei")

# 4
with open("log.txt", "r", encoding="utf-8") as f:
    evenimente = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    ultimul_error = None

    for linie in f:
        if "INFO" in linie:
            evenimente["INFO"] += 1
        elif "WARNING" in linie:
            evenimente["WARNING"] += 1
        elif "ERROR" in linie:
            evenimente["ERROR"] += 1
            ultimul_error = linie.strip()

    print(f"Numar evenimente INFO: {evenimente['INFO']}")
    print(f"Numar evenimente WARNING: {evenimente['WARNING']}")
    print(f"Numar evenimente ERROR: {evenimente['ERROR']}")
    if ultimul_error:
        print(f"Ultimul eveniment de tip ERROR: {ultimul_error}")
    else:
        print("Nu au fost evenimente de tip ERROR.")

# 5
with open("login.txt", "r", encoding="utf-8") as f:
    incerci_user = {}

    for linie in f:
        linie = linie.strip()
        if not linie:
            continue

        parti = linie.split("|")

        if len(parti) != 3:
            continue

        data_ora = parti[0].strip().replace("$", "")
        user = parti[1].strip().replace("@", "")
        status_text = parti[2].strip()

        # status is last word (passed / failed)
        status = status_text.split()[-1]

        if user not in incerci_user:
            incerci_user[user] = {
                "numar_incercari": 0,
                "ultima_data_ora_reusita": None
            }

        incerci_user[user]["numar_incercari"] += 1

        if status == "passed":
            incerci_user[user]["ultima_data_ora_reusita"] = data_ora


with open("user_attempts.txt", "w", encoding="utf-8") as f:
    for user, info in incerci_user.items():
        f.write(
            f"# {user} | {info['numar_incercari']} | {info['ultima_data_ora_reusita']}\n"
        )

print("Datele au fost salvate in 'user_attempts.txt'.")
