import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CRUD.CRUD_CLIENTE import CRUDCliente  
from CRUD.CRUD_PRODUCTO import CRUDProducto
from CRUD.CRUD_PRODUCTO_FERTILIZANTE import CRUDFertilizante
from CRUD.CRUD_CONTROL_PLAGAS import CRUDControlPlagas
from CRUD.CRUD_ANTIBIOTICOS import CRUDAntibioticos
from CRUD.CRUD_FACTURA import CRUDFactura
from UI.UI import Ui

def dirigir():
    crudFactura = CRUDFactura()
    crudCliente = CRUDCliente(crudFactura)
    crudFertilizante = CRUDFertilizante() 
    crudControlPlagas = CRUDControlPlagas()
    crudAntibioticos = CRUDAntibioticos()
    
    
    ui = Ui()  
    
    while True:
        ui.mostrarMenu()  
        opcion = ui.menu()  
        if opcion == 1:  
            nombre, cedula = ui.agregarCliente()  
            crudCliente.agregarCliente(nombre, cedula)  
            
        elif opcion == 2: 
            ui.mostrarMenuProducto()
            tipo_producto = ui.menuProducto()
           
            if tipo_producto == 1: 
                nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez = ui.agregarFertilizante()
                crudFertilizante.agregarFertilizante(nombreProducto, registroIca, frecuencia, precio, fechaUltimaVez)
            elif tipo_producto == 2: 
                nombreControlPlaga, registroIcaControlPlaga, frecuenciaControlPlaga, precioControlPlaga, periodoCarencia = ui.agregarControlPlagas()
                crudControlPlagas.agregarProductoControlPlagas(nombreControlPlaga, registroIcaControlPlaga, frecuenciaControlPlaga, precioControlPlaga, periodoCarencia)
            elif tipo_producto == 3: 
                nombreAntibiotico, dosis, tipoAnimal, precioAntibiotico = ui.agregarAntibiotico()
                crudAntibioticos.agregarAntibioticos(nombreAntibiotico, dosis, tipoAnimal, precioAntibiotico)
                
        elif opcion == 3:
            cedula = ui.buscarClientePorCedula()
            cliente = crudCliente.buscar_por_cedula(cedula)
            if cliente:
                crudFactura.listarFacturas(cliente)
                 
        elif opcion == 4: 
            cedula, productos, antibioticos = ui.venderProducto() 
            factura = crudCliente.venderProducto(cedula, productos, antibioticos)  

        elif opcion == 5:  
            print("Saliendo del programa.")
            break

if __name__ == '__main__':
    dirigir()
