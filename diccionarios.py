#Diccionarios{'llave':'valor'}
alumno={'num_cta':'316024118',
        'nombre':('Alonso', 'Sagrero', 'Granados'),
        'semestre': 1,
        'promedio':0.0,
        'materias' : ['CYP', 'algebra', 'calculo', 'geometria', 'introICO'],
        'regular' :True,
        'lagrimas_por_examen' : 5,
        'direccion':{
                'calle':'Rancho Sequito',
                'colonia':'Impulsora Popular Avicola',
                'numero':1000,
                'cp': 'Nezahualcoyotl',
                'estado':{
                    'id':15,
                        'nombre': 'Etado de Mexico',
                        'corto': 'EdoMex',
                    }
                }
        }

print(alumno['direccion']['estado']['nombre'][10::].upper())
alumno['lagrimas_por_examen'] = 10
print(alumno)
alumno['cursa_ingles']=True
print(alumno)

print(alumno['materias'][1].upper())
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][3::])

mi_lista=[['a','b'],['c',10],['d',True]]
diccionario = dict(mi_lista)
print(diccionario)

#Son mutables

alumno['cursa_ingles']=True
print(alumno)

#Funcion keys()

llaves= alumno.keys()
print(llaves)
for llave in llaves:
    print("------------")
    print(llave)
    print('.............')
    print(alumno[llave])
    print("++++++++++++")

#Funcion values

for val in alumno.values():
    print('....')
    print(val)
    print('+++++++++++++++')

#Funcion items()

for elem in alumno.items():
    print('....')
    print(val)
    print('+++++++++++++++')
    
