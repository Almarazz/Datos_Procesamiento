import time

segundos = int(input('Cantidad de segundos a esperar: '))
time.sleep(segundos)
print(f'Han transcurrido, por lo menos, {segundos} segundos')


horainicial = time.time()

for termino in range(10):
    time.sleep(segundos)
    
print('proceso simulado concluido')
duracion = time.time() - horainicial 
print(f'La duracion del proceso simulado fue de {duracion:.4f} segundos')
