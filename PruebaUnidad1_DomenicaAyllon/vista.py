class VistaOperacion:
    def menu(self):
        print("\n--- CINE PARAÍSO ---")
        print("1. Registrar función")
        print("2. Mostrar funciones")
        print("3. Vender boletos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()
        return opcion

    def solicitar_datos(self):
        pelicula = input("Nombre de la película: ").strip()
        precio = float(input("Precio del boleto: ").strip())
        asientos = int(input("Cantidad de asientos: ").strip())
        return pelicula, precio, asientos

    def solicitar_venta(self):
        codigo = int(input("Código de la función: ").strip())
        cantidad = int(input("Cantidad de boletos: ").strip())
        return codigo, cantidad

    def mostrar_funciones(self, lista):
        if not lista:
            print("No hay funciones registradas.")
        else:
            for funcion in lista:
                print(funcion)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)