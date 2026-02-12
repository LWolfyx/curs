import random
from geometry import area, perimeter

r = random.randint(1, 10)
a = random.randint(1, 10)
l = random.randint(1, 10)
w = random.randint(1, 10)

print("Circle area:", area.circle(r))
print("Circle perimeter:", perimeter.circle(r))
