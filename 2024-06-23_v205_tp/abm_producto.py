
def agregar_producto(productos, codigo, nombre, componentes, precio): #permite agregar un nuevo producto
    nuevo_producto = {"codigo": codigo, "nombre": nombre, "componentes": componentes, "precio": precio}
    productos.append(nuevo_producto)


def eliminar_producto(productos, codigo): #permite eliminar un producto existente
    for producto in productos:
        if producto["codigo"] == codigo:
            productos.remove(producto)

    
def modificar_precio(productos, codigo): #permite modificar el precio de un producto existente
    for producto in productos:
        if producto["codigo"] == codigo:
            nuevo_precio = float(input("\t\tIngrese el nuevo precio: "))
            producto["precio"] = (f"{nuevo_precio:.2f}")
            #print("Producto modificado exitosamente")    
            return
    print("\n\n\n\tProducto no encontrado")     
    
def actualizar_producto(productos, datos):  #sirve de apoyo para la función 3 que actualiza datos de un producto
    codigo, nombre, componentes, precio = datos  
    for producto in productos:
        if producto["codigo"] == codigo:
            producto["nombre"] = nombre if nombre != "" else producto["nombre"]
            producto["componentes"] = componentes if componentes != "" else producto["componentes"]
            
def obtener_datos(productos, codigo): #permite            
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None                
            