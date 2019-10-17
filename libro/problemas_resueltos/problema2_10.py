A = int(input("Escribe un numero entero positivo para A: "))
B = int(input("Ingrese un numero entero positivo para B: "))
C = int(input("Ingrese un numero entero positivo para C: "))
if A > B:
    if A > C:
        print(f"El valor de A es el mayor y es: {A} ")
    elif A == C:
        print("Los valores de A y C son iguales a {A} y son los mayores. ")
    else:
        print(f"El valor de C es el mayor y es de {C}. ")
elif A == B:
    if A > C:
        print(f"Los los valores de A y B son miguales a {A} y son los mayores. ")
    elif A == C:
        print(f"Los valores de A y B y C son iguales y tienen valor de {A}. ")
    else:
        print(f"El numero {C} es el mayor. ")
print("Fin del programa")
