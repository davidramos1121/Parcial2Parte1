class Ui:
    def mostrarMenu(self):
        print("FACTURACION AGRICOLA")
        print("1) Agregar cliente")
        print("2) Agregar producto")
        print("3) Buscar cliente")
        print("4) Vender producto")
        print("5) Salir")
    
    def menu(self):
        opcion = int(input("Ingrese la opcion: "))
        return opcion
    
    def agregarCliente(self):
        print("\nAgregar Cliente")
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cedula del cliente: ")
        return nombre, cedula
    
    def mostrarMenuProducto(self):
        print("\nRegistro de Producto")
        print("1. Control de Fertilizantes")
        print("2. Control de Plagas")
        print("3. Antibiotico")
    
    def menuProducto(self):
        tipo_producto = int(input("Ingrese la opcion: "))
        return tipo_producto

    
    def agregarProductoFertilizante(self):
        nombreProducto = input("Ingrese el nombre del fertilizante: ")
        registroIca = input("Ingrese el registro ICA del fertilizante: ")
        frecuencia = input("Ingrese la frecuencia de aplicacion (dias): ")
        precio = input("Ingrese el precio: ")
        fechaUltimaVez = input("Ingrese la fecha de ultima aplicacion (dias): ")
        return nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez
    
    def agregarProductoControlPlaga(self):
        nombreControlPlaga = input("Ingrese el nombre del producto de control de plagas: ")
        registroIcaControlPlaga = input("Ingrese el registro ICA del control de plagas: ")
        frecuenciaControlPlaga = input("Ingrese la frecuencia de aplicacion (dias): ")
        precioControlPlaga = input("Ingrese el precio: ")
        periodoCarencia = input("Ingrese el periodo de carencia: ")
        return nombreControlPlaga, registroIcaControlPlaga, frecuenciaControlPlaga, precioControlPlaga, periodoCarencia
    
    def agregarAntibiotico(self):
        nombreAntibiotico = input("Ingrese el nombre del antibiotico: ")
        dosis = input("Ingrese la dosis: ")
        tipoAnimal = input("Ingrese el tipo de animal: ")
        precioAntibiotico = input("Ingrese el precio del antibiotico: ")
        return nombreAntibiotico, dosis, tipoAnimal, precioAntibiotico
    
    
    def buscarClientePorCedula(self):
        cedula = input("Ingrese la cedula del cliente: ")
        return cedula
    
    
    def venderProducto(self):
        cedula = input("Ingrese la cedula del cliente: ")
        productos = []
        antibioticos = []

        while True:
            agregar_fertilizante = input("¿Desea agregar un fertilizante? (s/n): ").lower()
            if agregar_fertilizante == 's':
                nombre_fertilizante = input("Ingrese el nombre del fertilizante: ")
                productos.append({"tipo": "fertilizante", "nombre": nombre_fertilizante})
            elif agregar_fertilizante == 'n':
                break
        while True:
            agregar_control_plaga = input("¿Desea agregar un producto de control de plagas? (s/n): ").lower()
            if agregar_control_plaga == 's':
                nombre_control_plaga = input("Ingrese el nombre del producto de control de plagas: ")
                productos.append({"tipo": "control_plaga", "nombre": nombre_control_plaga})
            elif agregar_control_plaga == 'n':
                break
        while True:
            agregar_antibiotico = input("¿Desea agregar un antibiotico? (s/n): ").lower()
            if agregar_antibiotico == 's':
                nombre_antibiotico = input("Ingrese el nombre del antibiotico: ")
                antibioticos.append({"nombre": nombre_antibiotico})
            elif agregar_antibiotico == 'n':
                break

        return cedula, productos, antibioticos
