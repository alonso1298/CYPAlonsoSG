CATE = int(input("¿Cual es la categoria del trabajador (1-4)? : "))
SUE = float(input("¿Cual es tu sueldo? : "))
NSUE = 0 

if CATE == 1:
    NSUE = SUE * 1.05
    print("Esta categoria agrega 15% a tu sueldo")
elif CATE == 2:
    NSUE = SUE * 1.10
    print("Esta categoria agrega 10% a tu sueldo")
elif CATE == 3:
    NSUE = SUE * 1.08
    print("Esta categoria agrega 8% a tu sueldo") 
elif CATE == 4:
    NSUE = SUE * 1.07
    print("Esta categoria agrega 7% a tu sueldo")

print(f"Dada la categoria { CATE } el nuevo sueldo del trabajador es { NSUE }")
