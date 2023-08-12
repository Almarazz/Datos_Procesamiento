import random 
#Demostracion de randrange(), randint() y random()

print(f'Obteniendo un numero entero aleatorio que puede ir del 0 al 19: {random.randrange(20)}')
print(f'Obteniendo un numero entero aleatorio par que puede ir del 2 al 20: {random.randrange(2, 21, 2)}')
print(f'Obteniendo un numero entero aleatorio que puede ir del 1 al 20: {random.randint(1, 20)}')
print(f'Obteniendo un valor numerico entre 0.0 y 1.0 inclusive: {random.random()}')

ListaDePrueba = [10, 20, 30, 40, 15, 25, 32, 45]
print(f'La lista de prueba es {ListaDePrueba}')

print(f'El valor seleccionado aleatoriamente de la lista anterior es {random.choise(ListaDePrueba)}')

random.shuffle(ListaDePrueba)
print(f"La lista ya 'perturbada/barajada' es {ListaDePrueba}")