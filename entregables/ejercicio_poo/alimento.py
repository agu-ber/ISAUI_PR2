# Se importa la clase Producto
from producto import Producto

class Alimento(Producto):
    """
    Clase que representa un producto alimenticio, que es una clase hija de Producto.

    Atributos:
        nombre (str): Nombre o descripción del producto.
        precio (float): Precio del producto en pesos.
        cantidad (int): Cantidad disponible del producto.
        fecha_expiracion (str): Fecha de vencimiento del producto.
    """

    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        """
        Inicia una nueva instancia de la clase Alimento.

        Parámetros:
            nombre (str)
            precio (float)
            cantidad (int)
            fecha_expiracion (str)
        """
        super().__init__(nombre, precio, cantidad) # La función super() se usa para acceder a los atributos o métodos de la clase padre.
        self.fecha_expiracion = fecha_expiracion

    def get_fecha_expiracion(self):
        """
        Obtiene la fecha de vencimiento del producto.

        Devuelve:
            fecha_expiracion (str)
        """
        return self.fecha_expiracion
    
    def mostrar_info(self):
        """
        Obtiene la información completa del producto alimenticio, incluyendo la fecha de vencimiento.

        Devuelve:
            mensaje (str)
        """
        info_producto = super().mostrar_info()
        info_alimento = f"\nFecha de vencimiento: {self.get_fecha_expiracion()}" # Las f-strings (formatted string literals) son una manera concisa y eficiente de incluir expresiones dentro de cadenas de texto.
        mensaje = info_producto + info_alimento

        return mensaje