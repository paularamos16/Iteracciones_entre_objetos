from tienda import *
from producto import Producto
from general import  *


def main():
    limpiar()
    #crear la tienda
    print("Creando nueva tienda...\n\n")
    nom_tienda =input("ingrese el nombre de la tienda : ")
    try:
        delivery=float(input("ingrese valor de delivery: "))
    except ValueError:
        delivery=0
        print("el delivery queda en cero")
    tipo_tienda=input('''
        Seleccione que tipo de tienda quiere crear:
        1. Restaurante
        2. Supermercado
        3. Farmacia
        4. salir            
            
            escoja su opcion (1,2,3 o 4):    ''')
    if tipo_tienda=="1":
        mi_tienda=Restaurante(nom_tienda, delivery)
    elif tipo_tienda=="2":
        mi_tienda=Supermercado(nom_tienda, delivery)
    elif tipo_tienda=="3":
        mi_tienda=Farmacia(nom_tienda,delivery)
    elif tipo_tienda=="4":
        salir()
    else:
        print("la opcion seleccionada no es valida....")
        salir() 
    #menu de opciones de la tienda
    while True:
        limpiar()
        print(f"Menu de opciones Tienda: {mi_tienda.Nombre_Tienda}" )
        menu=input('''
            Seleccione  una opcion del menu  :
            1. Ingresar producto
            2. listar producto
            3. realizar venta
            4. salir            
                
                escoja su opcion (1,2,3 o 4):    ''')
        
        if menu == "1":
            limpiar()
            nom_producto=input("Ingrese nombre del nuevo producto: ")
            precio_prod=float(input("ingrese el precio del producto: "))
            try:
                stock_prod=float(input("ingrese el stock: "))
            except ValueError:
                stock_prod=0
            mi_producto=Producto(nom_producto,precio_prod,stock_prod)
            print(mi_producto )
            mi_tienda.ingresar_producto(mi_producto)
            print(f"{mi_producto.obtener_nombre.upper()} creado con exito")
            presionar_enter()
            
        elif menu == "2":
            limpiar()
            print("la lista de productos de esta tienda es:\n")
            print(mi_tienda)
            print(mi_tienda.listar_productos())
            presionar_enter()
        elif menu == "3":
            limpiar()
            nombre_producto=input("cual producto desea vender?")
            cantidad=float(input("cuantos articulos desea vender?"))
            mi_tienda.realizar_venta(nombre_producto,cantidad)
            presionar_enter()
        elif menu == "4":
            salir() 
        else:
            print("la opcion seleccionada no es valida....")
            salir()    
        
    
        
if __name__=="__main__":
    main()