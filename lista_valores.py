dias = ['lunes', 'martes', 'miercoles','jueves', 'viernes', 'sabado', 'domingo']

dias[1] ='MARTES'
print(dias)

dias[2:4] = ['MIERCOLES', 'JUEVES']
print(dias)

dias[4:]= ['VIERNES']
print(dias)

dias[0] = 'LUNES'
print(dias)

dias.append('otro')
print(dias)

dias.insert(2,'Otro mas')
print(dias)

print(dias.index('otro'))

print(dias[3])

print(dias)

dias.pop(6)
print(dias)

dias.remove('Otro mas')
print(dias)

dias.pop()
print(dias)

dias.clear()
print(dias)



