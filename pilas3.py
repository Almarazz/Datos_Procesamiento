stack = [] #Creamos una lista vacía, llamada stack
SEPARA = ("-" * 20) + "\n" #Se crea variable para separar cada menú, \n es salto de línea
#Creamos un Menú con 4 opciones
def main():
    print("1 Aplilar elemento (entero)")
    print("2 Desapilar elemento")
    print("3 Mostrar pila")
    print("4 Salir")
    print(SEPARA * 1)# Imprime la variable para separar los menús 
    option = input("Elija una opción: ")
    #Esta opción permite apilar el numero en la lista
    if str(option)=="1":
        elemento = input(" Introduzca el numero a apilar: ")
        stack.append(elemento)
        print("**- Elemento apilado -**")
        main()
    #Esta opción saca desapila a partir del último número ingresado
    elif str(option)=="2":
        if len(stack) == 0:
            print(" No hay elementos para desapilar ")
            main()
        else:
            print("**-El numero: ",stack.pop()," fue desapilado-**")
            main()
    #Esta opción imprime en pantalla la pila 
    elif str(option)=="3":
        for i in reversed(range(len(stack))):
            print("Pila: ",stack[i])
        main()
    #Esta opción permite salir de la ejecución del Código
    elif str(option)=="4":
        exit()
    else:
        print("\Opción incorrecta.\n")
        main()
main()