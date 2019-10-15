A = int(input("1er numero:"))
B = int(input("2do numero:"))
C = int(input("3er numero:"))

if A < B:
    if B < C:
        print(f"Los numeros estan en orden creciente")
    else:
        print(f"Los numeros no estan en orden creciente")
else:
    print(f"Los numeros no estan en orden creciente")
