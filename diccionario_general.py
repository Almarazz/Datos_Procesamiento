productos ={
    10:{
        "1d": 10,
        "desc":"Producto 10", 
        "precio": 2992.45
    },
    20:{
        "id": 20,
        "desc":"Productos 20",
        "precio": 834.55
    }   
}

referencia = 20

if referencia in productos.keys():
    datos = productos.get(referencia)
    print(datos)
    print(datos["id"])
    print(datos['desc'])
    print(datos["precio"])
    
