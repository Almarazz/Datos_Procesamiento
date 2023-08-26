pelis_favoritas = '[Eyes wide shut; The Godfather; The Professional; The Notebook]'

favoritas = pelis_favoritas
print(favoritas)
print(type(favoritas))

pelis_favoritas = '[Eyes wide shut | The Godfather | The Professional | The Notebook]'

favoritas = pelis_favoritas[1:-1].split('|')
print(favoritas)
print(type(favoritas))