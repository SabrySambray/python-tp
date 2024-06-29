import time
from pantalla import screen_clear
from time import sleep
from base_original import traer_productos # base de datos externa en base_datos.py
import keyboard
from colorama import init
from colorama import Fore, Back, Style
from logo import monty
from gracias import monty_chau
def ticket(ticket_db,ticket_total):
    medio_pago = "0" # "0" = sin medio de pago seleccionado / "1" medio de pago cancelado
    while True and medio_pago == "0":
        tag_fecha = time.strftime("%d/%m/%Y") # calcular fecha
        tag_hora = time.strftime("%H:%M:%S") # calcular hora
        screen_clear() # │ ─ ┌ ┐ └ ┘  
        print(Fore.BLACK + Back.WHITE + "\033[1m")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" MONTY BURGER                                       " + Back.LIGHTYELLOW_EX + " ******  Seleccione un método de pago  ****** ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" Av. Python 2024                        Visual Code " + Back.LIGHTYELLOW_EX + " ┌────────────┐ ┌────────────┐ ┌────────────┐ ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" CUIT 20-12345678-1         ING.BRUTOS 901-123456-2 " + Back.LIGHTYELLOW_EX + " │ T. CRÉDITO │ │ T. DÉBITO  │ │   QR/APP   │ ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f"             IVA RESPONSABLE INSCRIPTO              " + Back.LIGHTYELLOW_EX + " └────────────┘ └────────────┘ └────────────┘ ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" -------------------------------------------------- " + Back.LIGHTYELLOW_EX + "  Presione [T]   Presione [D]   Presione [Q]  ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" {tag_fecha} {tag_hora}          NRO.T.: 2229-01234567 " + Back.LIGHTRED_EX + "  Para cancelar la operación presione [ESC]   ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" -------------------------------------------------- ")
        for it in ticket_db:
            temp_format = format((it['cantidad'])*(float(it['precio'])),".2f")
            print(Fore.BLACK + Back.WHITE + "\033[1m" + f"       {it['cantidad']:<3} x {it['precio']:<11}                            ")
            print(Fore.BLACK + Back.WHITE + "\033[1m" + f" {it['codigo']:<5} {it['nombre']:<30}   {temp_format:>11} ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" -------------------------------------------------- ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f"                               TOTAL    {ticket_total:>11} ")
        print(Fore.BLACK + Back.WHITE + "\033[1m" + f" -------------------------------------------------- ")
        while True:
            if keyboard.is_pressed('t'):
                print(Back.LIGHTBLUE_EX + f" ¿ Desea pagar con tarjeta de credito ? (S/N) ")
                medio_pago = "t"
                break
            if keyboard.is_pressed('d'):
                print(Back.LIGHTBLUE_EX + f" ¿ Desea pagar con tarjeta de débito ? (S/N) ")
                medio_pago = "d"
                break
            if keyboard.is_pressed('q'):
                print(Back.LIGHTBLUE_EX + f" ¿ Desea pagar con QR/APP ? (S/N) ")
                medio_pago = "q"
                break
            if keyboard.is_pressed('esc'):
                print(Back.LIGHTRED_EX + f" Se canceló la operación. ")
                medio_pago = "1"
                sleep(5)
                break 
        while True and medio_pago != "1":
            if keyboard.is_pressed('s'):
                print("Medio de pago aceptado")
                sleep(5)
                break
            else:
                if keyboard.is_pressed('n'):
                    print("Medio de pago cancelado, seleccione nuevamente")
                    sleep(5)
                    medio_pago = "0"
                    break
    
    print(f" Presione la tecla [C] para continuar. ") 
    while True:
        if keyboard.is_pressed('c'):break
    monty_chau()
    sleep(5)
    
def main():
    carrito_db = []
    producto = traer_productos() # importar productos de base externa
    screen_clear()
    cantx = 0
    indice_p = 0
    prod2_subtotal = 0
    producto_cant = 1
    while indice_p < len(producto): # loop recorrido diccionario de productos
        screen_clear()
        prod2_subtotal = format(float(producto[indice_p]['precio']) * float(producto_cant),".2f")
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m")
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + "┌" + " " * 100 + "┐")  # │ ─ ┌ ┐ └ ┘ ^ v  ˄˅
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"  {producto[indice_p]['codigo']:<10}" + " " * 90)
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"  {producto[indice_p]['nombre']:<30}" + " " * 70)
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"  {producto[indice_p]['componentes']:<66}" + " " * 34)
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"  " * 51);tag_precio="Precio";tag_cant="Cant";tag_subtotal="Subtotal"
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"        {tag_precio:<10} {tag_cant:<5}           {tag_subtotal:<5}" + " " * 59)
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + f"  $ {producto[indice_p]['precio']:>10}    {producto_cant:>5}        $ {prod2_subtotal:>10}" + " " * 59)
        print(Fore.BLACK + Back.LIGHTMAGENTA_EX + "\033[1m" + "└" + " " * 100 + "┘") # │ ─ ┌ ┐ └ ┘         
        print(Fore.LIGHTRED_EX + "Utilice las flechas del teclado para navegar los productos")
        print("<" + Fore.CYAN + "  Cursor Izquierdo (Cambiar de producto)")
        print(">" + Fore.CYAN + "  Cursor Derecho   (Cambiar de producto)")
        print("˄" + Fore.CYAN + "  Cursor Arriba    (+ cantidad)")
        print("˅" + Fore.CYAN + "  Cursor Abajo     (- cantidad)") 
        print("ESPACIO" + Fore.LIGHTCYAN_EX + "  Seleccionar")
        print("ESC" + Fore.LIGHTCYAN_EX + "  Cancelar")
        print("ENTER" + Fore.LIGHTCYAN_EX + "  Aceptar compra y elegir medio de pago")
        print("DELETE / SUPRIMIR" + Fore.LIGHTCYAN_EX + "  Eliminar último ítem del carrito")        
        print("─" * 135)
        carrito_total = 0
        temp_format = 0
        if len(carrito_db) > 0:
            tag_cod="Cod";tag_nombre="Nombre";tag_componentes="Componentes";tag_precio="Precio";tag_cant="Cant";tag_subtotal="Subtotal"
            print(f"{tag_cod:<5}{tag_nombre:<30}{tag_componentes:<66}  {tag_precio:>10}  {tag_cant :>5}    {tag_subtotal:>11}")
            print("─" * 135)
            for i in carrito_db:
                temp_format = format((i['cantidad'])*(float(i['precio'])),".2f")
                print(f"{i['codigo']:<5}{i['nombre']:<30}{i['componentes']:<66} ${i['precio']:>10}  {i['cantidad']:>5}   ${temp_format:>11}")
                carrito_total = carrito_total + ((i['cantidad'])*(float(i['precio'])))
            temp_format = format(carrito_total,".2f")
            print(f"\nTOTAL = $ " + str(temp_format))
        while True: # while teclado
            try:
                if keyboard.is_pressed('up'): # tecla cursor arriba
                    producto_cant = producto_cant + 1
                    sleep(0.1)    
                    break # salir de while teclado
                if keyboard.is_pressed('down'): # tecla cursor abajo
                    if producto_cant > 1:
                        producto_cant = producto_cant - 1
                    sleep(0.1)                            
                    break # salir de while teclado   
                if keyboard.is_pressed('right'): # tecla cursor derecho
                    producto_cant = 1 ##
                    indice_p = indice_p + 1
                    if indice_p > len(producto) - 1:
                        indice_p = 0
                    sleep(0.2)    
                    break # salir de while teclado
                if keyboard.is_pressed('left'): # tecla cursor izquierdo
                    producto_cant = 1 ##              
                    indice_p = indice_p - 1
                    if indice_p < 0:
                        indice_p = len(producto) - 1
                    sleep(0.2)                            
                    break # salir de while teclado   
                if keyboard.is_pressed('esc'): # tecla escape
                    producto_cant = 1 ##                    
                    indice_p = len(producto) + 1
                    sleep(0.2)                
                    print("Pedido Cancelado")            
                    break # salir de while teclado
                if keyboard.is_pressed('space'): # tecla espacio              
                    if len(carrito_db) < 10:
                        print(f"Producto seleccionado {producto[indice_p]['codigo']:<8}")
                    else:
                        print(Fore.WHITE+Back.RED+" Límite de 10 productos alcanzado "+Style.RESET_ALL)# Limite de 10 items en rojo
                    sleep(0.3)
                    cantx = producto_cant
                    producto_cant = 1                    
                    if cantx > 0 and len(carrito_db) < 10:
                        temp_carrito = {"codigo": producto[indice_p]['codigo'],"nombre": producto[indice_p]['nombre'],"componentes": producto[indice_p]['componentes'],"precio": producto[indice_p]['precio'],"cantidad": cantx}
                        carrito_db.append(temp_carrito)
                    break # salir de while teclado
                if keyboard.is_pressed('enter') and carrito_total > 0: # si tecla enter y si hay items a facturar
                    sleep(0.3)
                    ticket(carrito_db,temp_format)# ir a pantalla ticket y medios de pago
                    break # salir de while teclado
                if keyboard.is_pressed('delete'): # tecla delete
                    sleep(0.3)                 
                    carrito_db.pop(len(carrito_db)-1)      
                    break # salir de while teclado
            except:
                break # ante cualquier otro error sale del while

init(autoreset=True)
monty()
input(Style.BRIGHT + Fore.GREEN + "                        Presione ENTER para continuar ")
main()
screen_clear()
