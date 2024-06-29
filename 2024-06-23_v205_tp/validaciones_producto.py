def validar_nuevo_producto(productos, codigo, nombre): #Evita agregar un producto con datos ya existentes
    for producto in productos:
        if producto["codigo"] == codigo:
            return f"""\n {'*' * 45} Ya existe un producto con el código: {codigo} {'*' * 45}"""
        elif producto["nombre"] == nombre:
            return f"""\n {'*' * 45} Ya existe un producto con el nombre: {nombre} {'*' * 45}"""
    return None    
            
def validar_codigo(productos, codigo): #Permite validar que no exista el código ingresado
    for producto in productos:
        if producto["codigo"] == codigo:
            return None
    #return f"""\t\t{'▓' * 52}\n\t\t▓   No existe un producto con el código: {codigo}   ▓\n\t\t{'▓' * 52}"""    
    return f"""\n\n\t\tNo existe un producto con el código: {codigo}"""
