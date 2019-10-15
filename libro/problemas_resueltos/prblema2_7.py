A = float(input("Variable A:"))
B = float(input("Variable B:"))
C = float(input("Variable C:"))

DIS = B ** 2 - 4 * A * C
if DIS >= 0:
    X1 = ((-B) + DIS ** 0.5) / 2 * A)
    X2 = ((-B) - DIS ** 0.5) / 2 * A)
    print(f"Las raices reales son { X1 } y { X2 } con distancia { DIS }")

