class Funcion:
    def __init__(self, codigo, pelicula, precio, asientos):
        self.codigo = codigo
        self.pelicula = pelicula
        self.precio = precio
        self.asientos = asientos

    def vender_boletos(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero.")
            return False
        if cantidad > self.asientos:
            print(f"Error: solo hay {self.asientos} asientos.")
            return False

        self.asientos -= cantidad
        print(f"Listo. Quedan {self.asientos} asientos.")
        return True

    def __str__(self):
        return f"[{self.codigo}] {self.pelicula}, Precio: ${self.precio}, Asientos: {self.asientos}"

class ListaFunciones:
    def __init__(self):
        self.listaFunciones = []
        self.cargar_datos()

    def cargar_datos(self):
        datos = [Funcion(1, "Toy Story", 4.50, 60),
                 Funcion(2, "Coco", 4.00, 45)]
        for f in datos:
            self.listaFunciones.append(f)

    def registrar_funcion(self, codigo, pelicula, precio, asientos):
        self.listaFunciones.append(Funcion(codigo, pelicula, precio, asientos))
        return print("Funcion registrada correctamente")

    def vender_funcion(self, codigo, cantidad):
        for funcion in self.listaFunciones:
            if funcion.codigo == codigo:
                return funcion.vender_boletos(cantidad)

    def mostrar_lista(self):
        return self.listaFunciones