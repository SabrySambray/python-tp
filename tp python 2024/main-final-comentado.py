from abm_producto import agregar_producto, eliminar_producto, modificar_precio, actualizar_producto, obtener_datos
from entrada_salida_producto import mostrar_menu_administracion, listar_productos, pedir_datos, mostrar_respuesta, confirmar, pedir_codigo, actualizar_datos, mostrar_datos, despedir, mostrar_error
import entrada_salida_producto as esp
from validaciones_producto import validar_nuevo_producto, validar_codigo
from base_datos_x_5 import traer_productos
import colorama
from colorama import Fore, Style
from logo import mostrar_logotipo

def main():
    productos = traer_productos() #Trae los productos desde la base de datos
    while True:
        opcion = mostrar_menu_administracion() #Muestra las opciones del menú
        
        match opcion:
            case "1": #Agrega un producto al listado
                codigo, nombre, componentes, precio = pedir_datos()
                respuesta = validar_nuevo_producto(productos, codigo, nombre)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    agregar_producto(productos, codigo, nombre, componentes, precio)
                    confirmar()
                    
            case "2": #Elimina un producto del listado
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    eliminar_producto(productos, codigo)
                    confirmar() 
                    
            case "3": #Actualiza datos de un producto
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    datos = actualizar_datos(productos, codigo)
                    actualizar_producto(productos, datos)
                    confirmar()   
                    
            case "4": #Permite modificar el precio de un producto sin actualizar otros datos
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    nuevo_precio = modificar_precio(productos, codigo)
                    confirmar()    
                                  
            case "5": #Muestra el listado de productos completo
                listar_productos(productos)
                
            case "6": #Muestra los datos de un producto elegido por su código
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    producto = obtener_datos(productos, codigo)
                    mostrar_datos(producto)
                    
            case "7": #Filtra el listado por categoría ingresando el nombre del valor
                categoria = input(f"""\n\t\t\t\033[36m 
                                sánguches
                                guarniciones
                                bebidas
                                ensaladas
                                postres
                                
                                Escriba el nombre de la categoría:\033[0m""")
                esp.mostrar_productos_por_categoria(categoria) #esp es la simplificación de entrada salida productos "as"
                        
                
            case "8": 
                mostrar_logotipo() #Muestra el logo de la marca y desarrolladores
                despedir() #Despide al usuario
                break               
            case _:
                mostrar_error() #Muestra un cartel de error

main()