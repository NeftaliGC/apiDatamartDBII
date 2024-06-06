from src.database.Connection import Connection
from src.database.resumenVentasProducto import ResumenVentasProducto

class Functions:

    def __init__(self):
        self.connection = Connection()

    def connect(self):
        return self.connection.connect()

    def resumen_ventas_producto(self, fecha_inicio, fecha_fin, nombre_producto):
        self.res = ResumenVentasProducto(fecha_inicio, fecha_fin, nombre_producto)
        return self.res.getResumenVentasProducto()