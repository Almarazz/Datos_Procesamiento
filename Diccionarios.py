peliculas ={
    10:'The GodFather',
    20:"Jurassic park'}",
    30:'Ex-Machina',
    40:'The Notebook'
}

print(len(peliculas))
print(peliculas.keys())
print(peliculas.values())


print(peliculas[40])
print(peliculas.get(40))

print(peliculas.items())

peliculas[50] = 'Star Wars'
peliculas.update({60:"Unknown"})
print(peliculas)

peliculas[60] = 'Casino Royale'
print(peliculas)

for llave in peliculas:
    print(llave)
    
for llave in peliculas:
    print(peliculas[llave])
    
for llave in peliculas.keys():
    print(llave)
    
for valor in peliculas.values():
    print(valor)
    
for llave,valor in peliculas.items():
    print(f'A la llave {llave} le corresponde el valor {valor}')
    
print(peliculas)
lo_mismo = peliculas
peliculas[80] = "fitch element"
print(lo_mismo)

peliculas_1 = peliculas.copy()
peliculas_1[90] = "Toy Story"
print(peliculas)
print(peliculas_1)

peliculas_2 = dict(peliculas)
peliculas_2 [90] = "Sharknado"

print(peliculas)
print(peliculas_2)



