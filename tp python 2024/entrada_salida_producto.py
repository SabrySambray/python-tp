import colorama
from base_datos_x_5 import traer_productos
from tabulate import tabulate
import pandas as pd
def mostrar_menu_administracion(): #Muestra el menú disponible para el usuario administrador
    print(f"""\n\n\nReferencias\nCategorías: \n\t\t1000 a 1999: Sánguches\n\t\t2000 a 2999: Guarniciones\n\t\t3000 a 3999: Bebidas\n\t\t4000 a 4999: Ensaladas\n\t\t5000 a 5999: Postres\n\n\n""")
    print(f"""\t    {'█' * 27}\n\t    █   MENÚ ADMINISTRACIÓN   █\n\t    {'█' * 27}""")
    print("\n\n\n\t\t1. Agregar producto")    
    print("\t\t2. Eliminar producto")
    print("\t\t3. Actualizar datos del producto")
    print("\t\t4. Modificar precio")
    print("\t\t5. Listado de productos")
    print("\t\t6. Ver datos de un producto")
    print("\t\t7. Submenú filtrar por categoría")
    print("\t\t8. Salir")
    return input("\n\t\tIndique la operación a realizar » ")

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
    #Pongo el texto en verde y cierro la solicitud para que el resto de texto siga siendo blanco
    print(f"""\n\n\t    ╔{'═' * 36}╗
\t    ║   \033[92mOperación realizada con éxito.   \033[0m║
\t    ╚{'═' * 36}╝""")
    
def pedir_codigo(): #Esta función sirve para pedir y luego validar un código
    codigo = input("\n\n\t\tIngrese el código del producto: ")      
    return codigo

def actualizar_datos(productos, codigo): #Permite actualizar los datos de un prod en la opción 3, Actualizar producto
    for producto in productos:
        if producto["codigo"] == codigo:
            nombre = producto["nombre"]
            #con el código [4 subrayo, luego punto y coma y el 36 es el cian y al final [0 le hago un reset al estilo
            print(f"\n\n\t\t\033[4;36mNombre\033[0m: {nombre}")
            nombre_actualizado = input("\t\tIngrese el nuevo nombre o presione <Enter> para aceptar: ").upper()
            #con el código [4 subrayo, luego punto y coma y el 36 es el cian y al final [0 le hago un reset al estilo        
            print(f"\n\t\t\033[4;36mComponentes\033[0m: {producto['componentes']}")
            componente_actualizado = input("\t\tIngrese el nuevo componente o presione <Enter> para aceptar: ").capitalize()      
    return codigo, nombre_actualizado, componente_actualizado, producto['precio']


        
def listar_productos(productos): #Permite ver el listado completo de productos
    print("▄" * 128)
    print(f"{'Código':^8}│{'Producto':<24}│{'Componentes':<84}│{'Precio ':>8}")
    print("▄" * 128)
    for producto in productos:
        print(f"{producto['codigo']:^8}│{producto['nombre']:<24}│{producto['componentes']:<84}│${producto['precio']:>7}")    
    
def mostrar_datos(producto): #Sirve para mostrar los datos de un prod en la opción 6, Ver datos de un producto
    etiquetas = ["Código", "Nombre", "Componentes", "Categoría", "Precio"]
    print(f"\n\t\t\033[92m{'═' * 80}\033[0m")
    for etiqueta, valor in zip(etiquetas, producto.values()):
        print(f"\t\t{etiqueta}: {valor}")
    print(f"\t\t\033[92m{'═' * 80}\033[0m")         
    
def despedir(): #Despide al usuario
    print(f"""\t  \033[33m  ╔{'═' * 48}╗
\t    ║{' ' * 5}Gracias por utilizar nuestro sistema{' ' * 7}║ 
\t    ║{' ' * 18} Hasta luego{' ' * 18}║
\t    ╚{'═' * 48}╝\033[0m""")

def mostrar_error(): #Avisa que hay un error en la opción seleccionada #Con el \033[91m doy inicio al color rojo y con el \033[0m hag un reset para que el texto vuelva a blanco
    print(f"""\n\n\t  ╔{'═' * 70}╗
\t  ║{' ' * 32}ERROR{' ' * 33}║ 
\t  ║    \033[91m Por favor, verifique la opción ingresada e intente nuevamente.   \033[0m║
\t  ╚{'═' * 70}╝""")
    
def mostrar_productos_por_categoria(categoria): #Esta función permite filtrar los productos según la categoría, pero hay que ingresar el nombre del "valor"
    productos_db = traer_productos()
    productos_filtrados = [producto for producto in productos_db if producto['categoria'] == categoria]
    df = pd.DataFrame(productos_filtrados)
    print(tabulate(df[['codigo', 'nombre', 'componentes', 'precio']], headers='keys', tablefmt='fancy_grid', showindex=False))

