operaciones_A = {
    12922: "Cliente 1",
    27728: "Cliente 2",
    28939: "Cliente 3"
    
}

operaciones_B = {
    12922: "Cliente 1",
    73772: "Cliente 4",
    46677: "Cliente 5"
}

operaciones_C = operaciones_A.copy()

for llave,valor in operaciones_B.items():
    if (not llave in operaciones_C.keys()):
        operaciones_C[llave] = valor
        
print(operaciones_C)
print(len(operaciones_C))