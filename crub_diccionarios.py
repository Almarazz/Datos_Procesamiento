Asistentes={}

Asistentes.update({"1234":["1234","Juan",100.00]})
Asistentes.update({"2345":["2345","María",400.00]})
Asistentes.update({"3456":["3456","Brenda",350.00]})

print(Asistentes)

print("\nMenú de opciones:")
print("\t[A] Agregar")
print("\t[B] Buscar")
print("\t[E] Eliminar elemento")
print("\t[M] Modificar elemento")
print("\t[V] Ver datos")
print("\t[Q] Quitar todos los elementos de la lista")
print("\t[S] Salir")

while True:
    opcion=input("\n¿QUÉ DESEAS HACER?: ")
    
    if (not opcion.upper()in "ABEMVQS"):
        print("Opcion no valida, intenta de nuevo ")
        continue
    
    if (opcion.upper()=="S"):
        print("Fin de la ejecucion.")
        break
    
    if (opcion.upper()=="A"):
        socio=input("Número de socio a agregar: ")
        
        if Asistentes.get(socio)==None:
            nombre=input("Nombre del socio: ")
            aportacion=float(input("Aportación: "))
            Asistentes.update({socio:[socio,nombre,aportacion]})
            print("Asistente agregado.")
        else:
            print("Asistente encontrado. no se puede repetir.")
            
    if (opcion.upper()=="B"):
        socio=input("Número de socio a buscar: ")
        recuperado=Asistentes.get(socio)
        if recuperado==None:
            print("Asistente no encontrado.")
        else:
            print(f"{recuperado[0]},{recuperado[1]},{recuperado[2]}")
    if (opcion.upper()=="E"):
        socio = input('Numero de socio a eliminar')
        if Asistentes.get(socio)==None:
            print("Asistente no encontrado. No se puede eliminar.")
        else:
            Asistentes.pop(socio)
            print("Asistente eliminado.")
            
    if (opcion.upper()=="M"):
        socio=input("Número de socio a modificar: ")
        
        recuperado=Asistentes.get(socio)
        if recuperado==None:
            print("Asistente no encontrado. No se puede modificar")
        else:
            print(f"Datos actuales: {recuperado[0]},{recuperado[1]},{recuperado[2]}")
            nombre=input("Nuevo nombre del socio: ")
            aportacion=float(input("Nueva aportación: "))
            Asistentes.update({socio:[socio,nombre,aportacion]})
            print("Asistente modificado.")
            
    if (opcion.upper()=="V"):
        acumulado=0.0
        print(f"Elementos en la lista: {len(Asistentes)} ")
        for v in Asistentes.values():
            print(f"{v[0]},{v[1]},{v[2]}")
            acumulado+=v[2]
            print(f"Acumulado: ${acumulado:,.2f} ")
            
    if (opcion.upper()=="Q"):
        print("Todos los asistentes eliminados.")

    

    

    
 
    
            

    
        
