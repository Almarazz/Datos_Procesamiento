import math


ValorFlotante = float(input('Introduce un valor con fracion decimal: \n'))

print(f'El siguiente entero hacia abajo de {ValorFlotante} es {math.floor(ValorFlotante)}')
print(f'El siguiente entero hacia arriba de {ValorFlotante} es {math.ceil(ValorFlotante)}')
print(f'La parte entera trunca de  {ValorFlotante} es {math.trunc(ValorFlotante)}')

ValorNumerico = int(input('\nDame un valor entero: \n'))
print(f'La raiz cuadrada es {ValorNumerico} es igual a {math.sqrt(ValorNumerico)}')
print(f'El Factorial de {ValorNumerico} es igual a {math.factorial(ValorNumerico)}')

