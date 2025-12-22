# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".
# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")
# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)

# 31
n = int(input("Introducere numar n: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 32
text = input("Introducere text: ")
cuvinte = text.split()
cuvinte_inversate = [cuvant[::-1] for cuvant in cuvinte]
text_inversat = "".join(cuvinte_inversate)
print(text_inversat)

# 33
numere_text = input("Numere: ")
numere_str = numere_text.split
numere = [int(numar) for numar in numere_str]
medie = sum(numere) / len(numere)
print("Media numerelor este: ", medie)
