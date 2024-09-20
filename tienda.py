from producto import Producto


class Tienda():
    def __init__(self, nombre_tienda, costo_delivery):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.__productos = []
        
    @property
    def Nombre_Tienda(self):
        return self.__nombre_tienda
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    @property
    def productos(self):
        return self.__productos
    
        
    def ingresar_producto(self, arg_producto):
        for prod in self.__productos:    #lo usamos asi porque estamos en la misma clase
            if prod.obtener_nombre.lower()==arg_producto.obtener_nombre.lower():
                if isinstance(self,Restaurante):
                    prod.obtener_stock=0
                else:    
                    prod.obtner_stock += arg_producto.obtener_stock
                    return
            
            if isinstance(self,Restaurante):
                prod.obtener_stock=0
            
            self.__productos.append(arg_producto)
                
                
                
    
    def listar_productos(self):
        pass
    
    
    def realizar_venta(self,nombre_producto,cantidad):
    #validar que el producto exista
        for prod in self.__productos:
            if prod.obtener_nombre.lower() == nombre_producto.obtener_nombre.lower():
                if isinstance(self, Restaurante):
                    print(f"el total de la venta es: {cantidad * prod.obtener_precio}.")
                    print("\nventa realizada con exito")
                else:
                    if cantidad <= prod.obtener_stock:
                        prod.obtener_stock -= cantidad   
                        print(f"el total de la venta es: {cantidad * prod.obtener_precio}.")
                        print("\nventa realizada con exito")
                    else:
                        print(f"Advertencia: solo hay : {prod.obtener_stock} del producto :{prod.obtener_nombre} ")
                        print(f"el total de la venta es: {prod.obtner_stock * prod.obtener_precio}")
                        
                        print("\nventa realizada con exito")
                        prod.obtener_stock = 0
                    return
        return                
                        
                        

class Restaurante(Tienda):
    def __init__(self, nombre_tienda, costo_delivery):
        super().__init__(nombre_tienda, costo_delivery)
        
    def listar_productos(self):
        cadena=""
        print(self._Tienda__productos)
        for item in self._Tienda__productos:
            #cadena += f"{item.obtener_nombre}\t-\t{item.obtener_precio}\n"
            cadena =item
        return cadena
            
            

class Supermercado(Tienda):
    def __init__(self, nombre_tienda, costo_delivery):
        super().__init__(nombre_tienda, costo_delivery)

class Farmacia(Tienda):
    def __init__(self, nombre_tienda, costo_delivery):
        super().__init__(nombre_tienda, costo_delivery)

