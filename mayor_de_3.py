print("Dame 3 numeros")
a = int(input("Dame un numero"))
b = int(input("Dame el segundo numero"))
c = int(input("Dame el tercer numero"))
x = 0
if a >= b:
    x = a
else:
    x = b
if x >= c:
    x = x
else:
    x = c

print(f"El numero mayor es {x} ")


