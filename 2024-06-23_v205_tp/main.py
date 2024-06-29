from abm_producto import agregar_producto, eliminar_producto, modificar_precio, actualizar_producto, obtener_datos
from entrada_salida_producto import mostrar_menu_administracion, listar_productos, pedir_datos, mostrar_respuesta, confirmar, pedir_codigo, actualizar_datos, mostrar_datos, despedir, mostrar_error
from validaciones_producto import validar_nuevo_producto, validar_codigo
from base_datos import traer_productos







def main():
    productos = traer_productos()
    while True:
        opcion = mostrar_menu_administracion()
        
        match opcion:
            case "1":
                codigo, nombre, componentes, precio = pedir_datos()
                respuesta = validar_nuevo_producto(productos, codigo, nombre)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    agregar_producto(productos, codigo, nombre, componentes, precio)
                    confirmar()
                    
            case "2":
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    eliminar_producto(productos, codigo)
                    confirmar() 
            case "3":
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    datos = actualizar_datos(productos, codigo)
                    actualizar_producto(productos, datos)
                    confirmar()   
            case "4":
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    nuevo_precio = modificar_precio(productos, codigo)
                    confirmar()                  
            case "5":
                listar_productos(productos)
            case "6":
                codigo = pedir_codigo()
                respuesta = validar_codigo(productos, codigo)
                if respuesta is not None:
                    mostrar_respuesta(respuesta)
                else:
                    producto = obtener_datos(productos, codigo)
                    mostrar_datos(producto)
            case "7":
                despedir()
                break              
            case _:
                mostrar_error()
                
                    
                

main()