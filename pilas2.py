class Pila: # Creamos la clase
    def __init__(self):# __init__ método que inicializa los atributos del objeto que creamos
        self.items = []
    def estaVacia(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
 
    def extraer(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop()
 
    def incluir(self, item): # Metodo para insertar elementos a la pila
        self.items.append(item)
 
s = Pila() # Creamos una instancia de la pila 
s.incluir('hola')
s.incluir('verdadero')
s.incluir(1)
s.incluir('falso')
print(s.extraer())