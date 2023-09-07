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


