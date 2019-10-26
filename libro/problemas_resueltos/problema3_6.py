MAY = -100000
MEN = 100000
N = int(input("Ingresa la cantidad de numeros que se ingresaran: "))
I = 1
for I in range(1,N + 1,I):
    NUM = int(input("Ingresa un numero entero: "))
    if NUM > MAY:
        MAY = NUM
    if NUM < MEN:
        MEN = NUM
    I += 1
print(f"El valor maximo es: {MAY} y el minimo es: {MEN}.")
print("Fin del programa.")
