import operations
import random


a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"Random numbers: {a}, {b}")
print(f"Adunare: {operations.adunare(a, b)}")
print(f"Scadere: {operations.scadere(a, b)}")
print(f"Produs: {operations.inmultire(a, b)}")
print(f"Impartire: {operations.impartire(a, b)}")
