import datetime
import time



hora = datetime.time(10,20,30)
print(f'El tipo de objeto de la hora es {type(hora)}')
print(f'La hora es {hora}')
print(f'La hora de {hora} es {hora.hour}')
print(f'El miunto de {hora} es {hora.minute}')
print(f'El segundo de {hora} es {hora.second}')
print(f'EL microsegundo de {hora} es {hora.microsecond}')


fecha_actual = datetime.date.today()
print(f'El tipo de objeto de la fecha es {type(fecha_actual)}')
print(f'La fecha actual es {fecha_actual}')
print(f'El año actual es {fecha_actual.year}')
print(f'El mes acutal es {fecha_actual.month}')
print(f'El dia actual es {fecha_actual.day}')

fecha_capturada = input('Dime una fecha (dd/mm/aaaa): ')
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f'La fecha capturada se transformo a {fecha_procesada}')