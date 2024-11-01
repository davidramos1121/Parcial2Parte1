
class Ui: 
    def mostrarMenu(Self):
        print("FACTURACION AGRICOLA\n")
        print("1) Agregar cliente")
        print("2) Agregar producto")
        print("3) Buscar cliente")
        print("4) Vender producto")
        print("5) Salir")
        
    def menu(Self):
        while True: 
            try:
                opcion = int(input("Ingrese la opción: "))
                if 1 <= opcion <= 6:
                    return opcion
                else:
                    print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")      


    def agregarCliente(Self):
        print("\nAgregar Cliente\n")
        nombreCliente = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ") 
        return nombreCliente, cedula
    
   
    def mostrarMenuProducto(Self):
        print("\nRegistro de Producto")
        print("1. Control de Fertilizantes")
        print("2. Control de Plagas")
        print("3. Antibiótico")
        
    def menuProducto(Self):
         while True: 
            try:
                tipo_producto = int(input("Ingrese la opción: "))
                if 1 <= tipo_producto <= 3:
                    return tipo_producto
                else:
                    print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.") 
                
                
        
    def agregarProductoFertilizante(Self):
        
     nombre = input("Ingrese el nombre del fertilizante: ")
     registroIca = input("Ingrese el registro ICA del fertilizante: ")
     frecuencia = int(input("Ingrese la frecuencia de aplicación (dias): "))
     precio = float(input("Ingrese el precio: "))
     fechaUltimaVez = input("Ingrese la fecha de última aplicación (dias): ")
     return nombre, registroIca, frecuencia, precio, fechaUltimaVez
                
    def agregarProductoControlPlaga(Self):
        
     nombre = input("Ingrese el nombre del producto: ")
     registroIca = input("Ingrese el registro ICA del producto: ")
     frecuencia = int(input("Ingrese la frecuencia de aplicación (dias): "))
     precio = float(input("Ingrese el precio: "))
     periodoCarencia = input("Ingrese el periodo de carencia (dias): ")
     return nombre, registroIca, frecuencia, precio, periodoCarencia
 
    def agregarAntibiotico(Self):
        
     nombre = input("Ingrese el nombre del producto: ")
     dosis = input("Ingrese la dosis del producto: ")
     tipoAnimal= int(input("Ingrese el tipo de animal a aplicar: "))
     precio = float(input("Ingrese el precio: "))
     return nombre, dosis,tipoAnimal,precio
     
    
    def venderProducto(Self):
        
        print("\nVenta de Producto\n")
        cedula = input("Ingrese la cédula del cliente: ")
        productos = []  
        antibioticos = []  

        agregar_fertilizante = input("¿Desea agregar un fertilizante? (s/n): ")
        
        while agregar_fertilizante.lower() == 's':
            nombre_fertilizante = input("Ingrese el nombre del fertilizante: ")
            productos.append(nombre_fertilizante)
            agregar_fertilizante = input("¿Desea agregar otro fertilizante? (s/n): ")
            
        agregar_control_plaga = input("¿Desea agregar un producto de control de plagas? (s/n): ")
        
        while agregar_control_plaga.lower() == 's':
            nombre_control_plaga = input("Ingrese el nombre del producto de control de plagas: ")
            productos.append(nombre_control_plaga)
            agregar_control_plaga = input("¿Desea agregar otro producto de control de plagas? (s/n): ")

        agregar_antibiotico = input("¿Desea agregar un antibiótico? (s/n): ")
        while agregar_antibiotico.lower() == 's':
            nombre_antibiotico = input("Ingrese el nombre del antibiótico: ")
            antibioticos.append(nombre_antibiotico)
            agregar_antibiotico = input("¿Desea agregar otro antibiótico? (s/n): ")

        return cedula, productos, antibioticos

            