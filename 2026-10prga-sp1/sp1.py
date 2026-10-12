#Kód žáka: 25
#Datum: 12.10.2026
#Tento program vytváří animaci pohybující se kuličky a počítá tabulku mocnin a odmocnin.
import time
import math

pocet = 8
print("Kulička jede.")

for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)

for i in range(pocet - 2, 0, -1):
    print(" " * i + "O")
    time.sleep(0.1)

print("\nTabulka")

for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))