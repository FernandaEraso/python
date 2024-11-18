# Integrantes: 
# Leidy Fernanda Eraso Vásquez
# Sarah Esther Calderón Legarda

# inicio clase producto
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad #contador de la cantidad

    def mostrar_detalles(self):
        print(f'Producto: {self.nombre} | Cantidad: {self.cantidad} | El precio del producto es: ${self.precio:.2f}')
# fin clase producto

# inicio clase inventario
class Inventario:
    def __init__(self):
        self.productos = {}
        self.historial_ventas = [] #almacena el historial

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].actualizar_cantidad(cantidad)
            print(f' La cantidad de {nombre} ha sido actualizada.') #actualiza la cantidad
        else: 
            self.productos[nombre] = Producto(nombre, cantidad, precio)
            print(f' El producto {nombre} se ha agregado al inventario.') #agregar producto

    def realizar_venta(self, nombre, cantidad):
        if nombre in self.productos: #verifica si el producto existe
            producto = self.productos[nombre] 
            if producto.cantidad >= cantidad: #verifica la cantidad disponible cpn la cantidad a vender
                producto.actualizar_cantidad(-cantidad) #actualiza la cantidad
                self.historial_ventas.append((nombre, cantidad, producto.precio)) 
                print(f'Venta de {cantidad} {nombre} realizada.') #realizar venta
                if producto.cantidad < 5:  # Limite stock bajo
                    print(f'Estimado usuario, el stock de {nombre} es bajo: {producto.cantidad} unidades.')
            else:
                print('La cantidad es insuficiente para realizar la venta, lo sentimos.')
        else:
            print('El producto no existe en el inventario, intente con otro nombre.')

    def consultar_inventario(self): #consultar inventario
        if self.productos:
            print('El inventario actual es:')
            for producto in self.productos.values(): #recorre el inventario
                producto.mostrar_detalles()
        else:
            print('El inventario está vacío.')

    def verificar_stock(self, limite):
        print(f'Los productos con stock menor al limite de {limite} es:')
        for producto in self.productos.values(): 
            if producto.cantidad < limite: #verifica si la cantidad es menor al limite
                producto.mostrar_detalles()

    def mostrar_historial_ventas(self): #mostrar historial de ventas
        if self.historial_ventas:
            print('Este es el historial de ventas:')
            for venta in self.historial_ventas: 
                print(f'Producto: {venta[0]} \n Cantidad: {venta[1]} \n Precio unitario: ${venta[2]:.2f}') #muestra el historial de ventas
        else:
            print('No hay ventas registradas en este momento, regresa cuando hayan ventas.')

# incio del menú
def menu():
    inventario = Inventario()
    while True:
        print("\n ════ Menú Gestión de Inventario ════")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Consultar inventario")
        print("4. Verificar productos bajos en stock")
        print("5. Mostrar historial de ventas")
        print("6. Salir")
# fin del menú
        # pedir seleccionar alguna de las opciones
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            try: 
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio por unidad: "))
                if cantidad > 0 and precio > 0: #valida que la cantidad y precio sean positivos
                    inventario.agregar_producto(nombre, cantidad, precio)
                else:
                    print("La cantidad y el precio deben ser positivos para que se acepten los valores.")
            except ValueError: 
                print("Opción inválida por favor, ingrese números válidos para cantidad y precio.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad a vender: "))
                if cantidad > 0:
                    inventario.realizar_venta(nombre, cantidad) #realiza venta
                else:
                    print("La cantidad de ventas debe ser positiva.") 
            except ValueError:
                print("Opción inválida por favor, ingrese un número válido.")
        elif opcion == '3':
            inventario.consultar_inventario() #muestra el inventario
        elif opcion == '4':
            try:
                limite = int(input("Ingrese el limite para verificar stock bajo: "))
                if limite >= 0:
                    inventario.verificar_stock(limite) #verifica stock bajo
                else:
                    print("El limite de stock debe ser un número positivo o cero.")
            except ValueError:
                print("Opción inválida, por favor ingrese un número válido.")
        elif opcion == '5':
            inventario.mostrar_historial_ventas() #muestra historial de ventas
        elif opcion == '6':
            print("Saliendo del sistema, que tengas un buen resto de día, vuelve pronto.")
            break
        else:
            print("Opción inválida, por favor seleccione una opción del menú.")

# Ejecutar el programa
if __name__ == "__main__": 
    menu() 
