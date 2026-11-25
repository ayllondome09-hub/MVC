class Funcion:
    def __init__(self, codigo, pelicula, precio, asientos):
        self.codigo = codigo
        self.pelicula = pelicula
        self.precio = precio
        self.asientos = asientos

    def vender_boletos(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero.")
        elif cantidad > self.asientos:
            print(f"Error: solo hay {self.asientos} asientos.")
        else:
            self.asientos -= cantidad
            print(f"Listo. Quedan {self.asientos} asientos.")

    def __str__(self):
        return f"[{self.codigo}] {self.pelicula} | Precio: ${self.precio} | Asientos: {self.asientos}"


def buscar_funcion(funciones, codigo):
    for funcion in funciones:
        if funcion.codigo == codigo:
            return funcion


def main():
    funciones = [
        Funcion(1, "Toy Story", 4.50, 60),
        Funcion(2, "Coco", 4.00, 45),
    ]

    while True:
        print("\n--- CINE PARAÍSO ---")
        print("1. Registrar función")
        print("2. Mostrar funciones")
        print("3. Vender boletos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pelicula = input("Nombre de la película: ")
            try:
                precio = float(input("Precio del boleto: "))
                asientos = int(input("Cantidad de asientos: "))
            except ValueError:
                print("Error: ingrese valores numéricos válidos.")
                continue

            if precio < 0 or asientos <= 0:
                print("Error: el precio no puede ser negativo y los asientos deben ser mayores a 0.")
                continue

            codigo = len(funciones) + 1
            funciones.append(Funcion(codigo, pelicula, precio, asientos))
            print(f"Registrado con el código {codigo}.")

        elif opcion == "2":
            if not funciones:
                print("No hay funciones registradas.")
            else:
                for funcion in funciones:
                    print(funcion)

        elif opcion == "3":
            try:
                codigo = int(input("Código de la función: "))
                cantidad = int(input("Cantidad de boletos: "))
            except ValueError:
                print("Error: ingrese números enteros válidos.")
                continue

            funcion = buscar_funcion(funciones, codigo)
            if funcion is None:
                print("Error: no existe ese código.")
            else:
                funcion.vender_boletos(cantidad)

        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida")


main()