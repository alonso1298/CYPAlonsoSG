# arreglos
# lectura
# escritura / Asignacion
# Actualizacion : inserpcion, eliminacion, modificacion
# rodenamiento
# busqueda
frutas = ["Zapote", "Manzanas" , "Pera" , "Aguacate" , "Durazno" , "Uva" , "Sandia"]

#lectura, el selector [ indice ]
print(frutas[2])
# lectura con for
# for op. 1
for indice in range (0, 7, 1):
    print(frutas[indice])
print("------")

# for op. 2 -- por un iterador for each

for fr in frutas:
    print(fr)

# asiganacion
frutas [2]="Melon"
print(frutas)
          
# insercion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"Limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)
# eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas [2]="Limon"
frutas.append("Limon")
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)

# ordenamiento
frutas.sort()
print(frutas)

# busqueda

print(f"La Uva esta en la pos. { frutas.index('Uva') } ")
print(f"El limon esta { frutas.count('Limon') } veces en la lista")

# concatenar
print(frutas)
otras_frutas = ["Rambutan", "Nispero", "Liche", "Pitaya"]
frutas.append(otras_frutas)
print(frutas)

# copiar

copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)



