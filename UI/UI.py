class Ui:
    def mostrarMenu(self):
        print("\nFACTURACION AGRICOLA")
        print("1) Agregar cliente")
        print("2) Agregar producto")
        print("3) Buscar cliente")
        print("4) Vender producto")
        print("5) Salir")

    def menu(self):
        opcion = int(input("Ingrese la opción: "))
        return opcion

    def agregarCliente(self):
        print("\nAgregar Cliente")
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        return nombre, cedula

    def buscarClientePorCedula(self):
        cedula = input("\nIngrese la cédula del cliente a buscar: ")
        return cedula

    def mostrarMenuProducto(self):
        print("\nRegistro de Producto")
        print("1. Control de Fertilizantes")
        print("2. Control de Plagas")
        print("3. Antibiótico")

    def menuProducto(self):
        opcion = int(input("Ingrese la opción: "))
        return opcion

    def agregarFertilizante(self):
        print("\nAgregar Fertilizante")
        nombre = input("Ingrese el nombre del fertilizante: ")
        registro_ica = input("Ingrese el registro ICA del fertilizante: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación (días): ")
        precio = input("Ingrese el precio: ")
        fecha_ultima_aplicacion = input("Ingrese la fecha de última aplicación (días): ")
        return nombre, registro_ica, frecuencia_aplicacion, precio, fecha_ultima_aplicacion

    def agregarControlPlagas(self):
        print("\nAgregar Control de Plagas")
        nombre = input("Ingrese el nombre del producto de control de plagas: ")
        registro_ica = input("Ingrese el registro ICA del producto de control de plagas: ")
        ingrediente_activo = input("Ingrese el ingrediente activo: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación (días): ")
        precio = input("Ingrese el precio: ")
        return nombre, registro_ica, ingrediente_activo, frecuencia_aplicacion, precio

    def agregarAntibiotico(self):
        print("\nAgregar Antibiótico")
        nombre = input("Ingrese el nombre del antibiótico: ")
        precio = input("Ingrese el precio: ")
        frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación (días): ")
        dosis = input("Ingrese la dosis recomendada: ")
        return nombre, precio, frecuencia_aplicacion, dosis

    def venderProducto(self):
        print("\nVenta de Producto")
        cedula = input("Ingrese la cédula del cliente: ")
        productos = []
        antibioticos = []

        # Recopilar productos
        while input("¿Desea agregar un fertilizante? (s/n): ").lower() == "s":
            nombre = input("Ingrese el nombre del fertilizante: ")
            productos.append({"tipo": "fertilizante", "nombre": nombre})
        while input("¿Desea agregar un producto de control de plagas? (s/n): ").lower() == "s":
            nombre = input("Ingrese el nombre del producto de control de plagas: ")
            productos.append({"tipo": "plaga", "nombre": nombre})

        # Recopilar antibióticos
        while input("¿Desea agregar un antibiótico? (s/n): ").lower() == "s":
            nombre = input("Ingrese el nombre del antibiótico: ")
            antibioticos.append({"nombre": nombre})

        return cedula, productos, antibioticos

    def listarFacturas(self):
        print("\nListando todas las facturas...")

    def buscarFactura(self):
        numero_factura = input("Ingrese el número de factura a buscar: ")
        return numero_factura



