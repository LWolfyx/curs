while True:
    print("===== MENIU =====")
    print("1. Adunare")
    print("2. Scadere")
    print("3. Inmultire")
    print("4. Impartire")
    print("5. Iesire")

    optiune = int(input("Alege o optiune: "))

    if optiune == 5:
        print("Iesire din program...")
        break

    if optiune in [1, 2, 3, 4]:
        a = float(input("Introdu primul numar: "))
        b = float(input("Introdu al doilea numar: "))

        if optiune == 1:
            print("Rezultat:", a + b)
        elif optiune == 2:
            print("Rezultat:", a - b)
        elif optiune == 3:
            print("Rezultat:", a * b)
        elif optiune == 4:
            if b != 0:
                print("Rezultat:", a / b)
            else:
                print("Eroare: impartire la zero!")
    else:
        print("Optiune invalida!")
