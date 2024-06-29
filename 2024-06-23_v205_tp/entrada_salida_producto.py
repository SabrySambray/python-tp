def mostrar_menu_administracion(): #Muestra el menú disponible para el usuario administrador
    print(f"""\n\n\nReferencias: \n\t\t1000 a 1999: Sánguches\n\t\t2000 a 2999: Guarniciones\n\t\t3000 a 3999: Bebidas\n\t\t4000 a 4999: Ensaladas\n\t\t5000 a 5999: Postres\n\n\n""")
    print(f"""\t\t{'█' * 27}\n\t\t█   MENÚ ADMINISTRACIÓN   █\n\t\t{'█' * 27}""")
    print("\n\n\n\t\t1. Agregar producto")    
    print("\t\t2. Eliminar producto")
    print("\t\t3. Actualizar datos del producto")
    print("\t\t4. Modificar precio")
    print("\t\t5. Listado de productos")
    print("\t\t6. Ver datos de un producto")
    print("\t\t7. Salir")
    return input("\n\n\n\t\tIndique la operación a realizar » ")

def pedir_datos(): #Sirve de apoyo para la función de agregar producto en la opción 1, Agregar producto
    codigo = input("\n\n\t\tIngrese el código del producto: ")
    nombre = input("\n\t\tIngrese el nombre del producto: ").upper()
    componentes = input("\n\t\tIngrese los componentes del nuevo producto: ").capitalize()
    precio = float(input("\n\t\tIngrese el precio del nuevo producto: "))
    precio = (f"{precio:.2f}")
    return codigo, nombre, componentes, precio
    
def mostrar_respuesta(mensaje): #Simplemente muestra el mensaje correspondiente
    print(mensaje)    
    
def confirmar(): #Confirma que la operación elegida fue realizada correctamente
    print(f"""\n {'*' * 45} Operación realizada con éxito. {'*' * 45}""")    
    
def pedir_codigo(): #Esta función sirve para pedir y luego validar un código
    # while True:    
    #     #le agrego una excepción con el try-except
    #     try:
    codigo = input("\n\n\t\tIngrese el código del producto: ")
            
        #     break
        # except:
        #     print("\t\tDebes ingresar un número entre el 1000 y el 5999")
        # if codigo <1000 or codigo >5999:
                
        #         print("\n\t\tEste comando precisa de un valor numérico entre el 1000 y el 5999. Intente nuevamente: ")
    #termina try-except        
    return codigo

def actualizar_datos(productos, codigo): #Permite actualizar los datos de un prod en la opción 3, Actualizar producto
    for producto in productos:
        if producto["codigo"] == codigo:
            nombre = producto["nombre"]
            print(f"Nombre: {nombre}")
            nombre_actualizado = input("Ingrese el nuevo nombre o presione <Enter> para aceptar: ").upper()
            print(f"Componentes: {producto['componentes']}")
            componente_actualizado = input("Ingrese el nuevo componente o presione <Enter> para aceptar: ").capitalize()      
    return codigo, nombre_actualizado, componente_actualizado, producto['precio']


        
def listar_productos(productos): #Permite ver el listado completo de productos
    print("▄" * 128)
    print(f"{'Código':^8}│{'Producto':<24}│{'Componentes':<84}│{'Precio ':>8}")
    print("▄" * 128)
    for producto in productos:
        print(f"{producto['codigo']:^8}│{producto['nombre']:<24}│{producto['componentes']:<84}│${producto['precio']:>7}")    

    
def mostrar_datos(producto): #Sirve para mostrar los datos de un prod en la opción 6, Ver datos de un producto
    etiquetas = ["Codigo", "Nombre", "Componentes", "Precio"]
    print("*" * 97)
    for etiqueta, valor in zip(etiquetas, producto.values()):
        print(f"{etiqueta}: {valor}")
    print("*" * 97)        
    
def despedir(): #Despide al usuario
    print(f"""""")
    print("Gracias por utilizar nuestro sistema.")
    print("Hasta luego")
  
def mostrar_error(): #Avisa que hay un error en la opción seleccionada
    print(f"""\t\t{'▓' * 70}▓   ERROR. \n\t\tPor favor, verifique la opción ingresada e intente nuevamente.  ▓\n\t\t{'▓' * 70}""")
    # print(f"""\n\n\t\tERROR.
    #       \tPor favor, verifique la opción ingresada e intente nuevamente.""")
    