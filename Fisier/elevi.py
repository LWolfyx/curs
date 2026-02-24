import json


def incarca_elevi():
    try:
        with open("elevi.txt", "r") as f:
            continut = f.read().strip()
            if not continut:
                return []
            return json.loads(continut)
    except FileNotFoundError:
        return []


def salveaza_elevi(elevi):
    with open("elevi.txt", "w") as f:
        json.dump(elevi, f, indent=4)


def calculeaza_media(nota_romana, nota_mate, nota_engleza):
    return round((nota_romana + nota_mate + nota_engleza) / 3, 2)


def adauga_elev(elevi):
    nume = input("Nume: ").lower()
    prenume = input("Prenume: ").lower()

    nota_romana = float(input("Nota romana: "))
    nota_mate = float(input("Nota mate: "))
    nota_engleza = float(input("Nota engleza: "))

    elev = {
        "nume": nume,
        "prenume": prenume,
        "nota romana": nota_romana,
        "nota mate": nota_mate,
        "nota engleza": nota_engleza,
        "media": calculeaza_media(nota_romana, nota_mate, nota_engleza)
    }

    elevi.append(elev)
    salveaza_elevi(elevi)
    print("Elev adaugat cu succes!")


def afiseaza_elevi(elevi):
    if not elevi:
        print("Nu exista elevi.")
        return

    for elev in elevi:
        print(f"{elev['nume']} {elev['prenume']} | "
              f"Romana: {elev['nota romana']} | "
              f"Mate: {elev['nota mate']} | "
              f"Engleza: {elev['nota engleza']} | "
              f"Media: {elev['media']}")


def sterge_elev(elevi):
    nume = input("Nume: ").lower()
    prenume = input("Prenume: ").lower()

    for elev in elevi:
        if elev["nume"] == nume and elev["prenume"] == prenume:
            elevi.remove(elev)
            salveaza_elevi(elevi)
            print("Elev sters.")
            return

    print("Elev negasit.")


def modifica_elev(elevi):
    nume = input("Nume: ").lower()
    prenume = input("Prenume: ").lower()

    for elev in elevi:
        if elev["nume"] == nume and elev["prenume"] == prenume:
            elev["nota romana"] = float(input("Nota romana noua: "))
            elev["nota mate"] = float(input("Nota mate noua: "))
            elev["nota engleza"] = float(input("Nota engleza noua: "))

            elev["media"] = calculeaza_media(
                elev["nota romana"],
                elev["nota mate"],
                elev["nota engleza"]
            )

            salveaza_elevi(elevi)
            print("Date modificate.")
            return

    print("Elev negasit.")


def meniu():
    elevi = incarca_elevi()

    while True:
        print("""
1. Adaugare elev
2. Afisare elevi
3. Modificare elev
4. Stergere elev
0. Iesire
""")

        opt = input("Alege optiune: ")

        if opt == "1":
            adauga_elev(elevi)
        elif opt == "2":
            afiseaza_elevi(elevi)
        elif opt == "3":
            modifica_elev(elevi)
        elif opt == "4":
            sterge_elev(elevi)
        elif opt == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida!")


meniu()
