# Se importa la clase Producto
from producto import Producto

class Electronico(Producto):
    """
    Clase que representa un producto electrónico, que es una clase hija de Producto.

    Atributos:
        nombre (str): Nombre o descripción del producto.
        precio (float): Precio del producto en pesos.
        cantidad (int): Cantidad disponible del producto.
        marca (str): Marca del producto.
        modelo (str): Modelo del producto.
    """

    def __init__(self, nombre, precio, cantidad, marca, modelo):
        """
        Inicia una nueva instancia de la clase Electrónico.

        Parámetros:
            nombre (str)
            precio (float)
            cantidad (int)
            marca (str)
            modelo (str)
        """
        super().__init__(nombre, precio, cantidad) # La función super() se usa para acceder a los atributos o métodos de la clase padre.
        self.marca = marca
        self.modelo = modelo

    def get_marca(self):
        """
        Obtiene la marca del producto.

        Devuelve:
            marca (str)
        """        
        return self.marca
    
    def get_modelo(self):
        """
        Obtiene el modelo del producto.

        Devuelve:
            modelo (str)
        """        
        return self.modelo
    
    def mostrar_info(self):
        """
        Obtiene la información completa del producto electrónico, incluyendo la marca y el modelo.

        Devuelve:
            mensaje (str)
        """
        info_producto = super().mostrar_info()
        info_electronico = f"\nMarca: {self.get_marca()}\nModelo: {self.get_modelo()}" # Las f-strings (formatted string literals) son una manera concisa y eficiente de incluir expresiones dentro de cadenas de texto.
        mensaje = info_producto + info_electronico

        return mensaje