class Producto:
    """
    Clase que representa un producto con un nombre, precio y cantidad.

    Atributos:
        nombre (str): Nombre o descripción del producto.
        precio (float): Precio del producto en pesos.
        cantidad (int): Cantidad disponible del producto.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicia una nueva instancia de la clase Producto.

        Parámetros:
            nombre (str)
            precio (float)
            cantidad (int)
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_nombre(self):
        """
        Obtiene el nombre del producto.

        Devuelve:
            nombre (str)
        """
        return self.nombre
    
    def get_precio(self):
        """
        Obtiene el precio del producto.

        Devuelve:
            precio (float)
        """
        return self.precio
    
    def get_cantidad(self):
        """
        Obtiene la cantidad disponible del producto.

        Devuelve:
            cantidad (int)
        """
        return self.cantidad
    
    def mostrar_info(self):
        """
        Obtiene la información completa del producto.

        Devuelve:
            mensaje (str)
        """
    
        # Las f-strings (formatted string literals) son una manera concisa y eficiente de incluir expresiones dentro de cadenas de texto.
        mensaje = (
            f"\nDatos del producto:\nNombre: {self.get_nombre()}"
            f"\nPrecio: {self.get_precio()}\nCantidad: {self.get_cantidad()}"
        )
        
        return mensaje