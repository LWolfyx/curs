import random
from geometry import area, perimeter

r = random.randint(1, 10)
a = random.randint(1, 10)
l = random.randint(1, 10)
w = random.randint(1, 10)
print(f"Random: r={r}, a={a}, l={l}, w={w}")
print("Arie cerc:", area.circle(r))
print("Perimetru cerc:", perimeter.circle(r))
print("Arie patrat:", area.square(a))
print("Perimetru patrat:", perimeter.square(a))
print("Arie dreptunghi:", area.rectangle(l, w))
print("Perimetru dreptunghi:", perimeter.rectangle(l, w))
