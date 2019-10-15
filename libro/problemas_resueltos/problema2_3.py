MAT = int(input("Numero de matricula:"))
CALI1 = float(input("Primera calificacion:"))
CALI2 = float(input("Segunda calificacion:"))
CALI3 = float(input("Tercera calificacion:"))
CALI4 = float(input("Cuarta calificacion:"))
CALI5 = float(input("Quinta calificacion:"))

PROM = (CALI1 + CALI2 + CALI3 + CALI4 + CALI5) / 5

if PROM >= 6:
    print(f"El alumno con numero de cuenta {MAT} tu promedio es { PROM } y estas aprobado!")
else:
    print(f"El alumno con numero de cuenta {MAT} tu promedio es { PROM } y estas reprobado")
