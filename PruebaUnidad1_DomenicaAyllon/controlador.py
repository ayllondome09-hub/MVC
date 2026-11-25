from PruebaUnidad1_DomenicaAyllon.modelo import ListaFunciones
from PruebaUnidad1_DomenicaAyllon.vista import VistaOperacion


class Controlador:
    def __init__(self):
        self.modelo = ListaFunciones()
        self.vista = VistaOperacion()

    def registrar(self):
        try:
            pelicula, precio, asientos = self.vista.solicitar_datos()
        except ValueError:
            self.vista.mostrar_mensaje("Error: ingrese valores numéricos válidos.")
            return

        if precio < 0 or asientos <= 0:
            self.vista.mostrar_mensaje("Error: el precio no puede ser negativo y los asientos deben ser mayores a 0.")
            return

        codigo = len(self.modelo.mostrar_lista()) + 1
        self.modelo.registrar_funcion(codigo, pelicula, precio, asientos)

    def vender(self):
        try:
            codigo, cantidad = self.vista.solicitar_venta()
        except ValueError:
            self.vista.mostrar_mensaje("Error: ingrese números enteros válidos.")
            return

        resultado = self.modelo.vender_funcion(codigo, cantidad)
        if resultado is None:
            self.vista.mostrar_mensaje("Error: no existe ese código.")

    def ejecutar(self):
        while True:
            opcion = self.vista.menu()

            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                self.vista.mostrar_funciones(self.modelo.mostrar_lista())
            elif opcion == "3":
                self.vender()
            elif opcion == "4":
                self.vista.mostrar_mensaje("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida")

controlador = Controlador()
controlador.ejecutar()