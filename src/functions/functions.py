from src.database.Connection import Connection
from src.database.resumenVentasProducto import ResumenVentasProducto
from src.database.resumenVentasFarmacia import ResumenVentasFarmacia
import matplotlib.pyplot as plt
import io
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Functions:

    def __init__(self):
        self.connection = Connection()

    def connect(self):
        return self.connection.connect()

    def resumen_ventas_producto(self, fecha_inicio, fecha_fin, nombre_producto):
        self.res = ResumenVentasProducto(fecha_inicio, fecha_fin, nombre_producto)
        return self.res.getResumenVentasProducto()

    def resumen_completo_ventas_producto(self):
        self.res = ResumenVentasProducto()
        return self.res.getResumenCompletoVentasProducto()

    def resumen_ventas_farmacia(self, fecha_inicio, fecha_fin, nombre_farmacia):
        self.res = ResumenVentasFarmacia(fecha_inicio, fecha_fin, nombre_farmacia)
        return self.res.getResumenVentasFarmacia()

    def resumen_completo_ventas_farmacia(self):
        self.res = ResumenVentasFarmacia()
        return self.res.getResumenCompletoVentasFarmacia()

    def desglose_ventas_producto(self, fecha_inicio, fecha_fin, nombre_producto):
        self.res = ResumenVentasProducto(fecha_inicio, fecha_fin, nombre_producto)
        return self.res.getDesgloseVentasProducto()

    def desglose_completo_ventas_producto(self):
        self.res = ResumenVentasProducto()
        return self.res.getDesgloseCompletoVentasProducto()

    def get_graphic_desglose(self):
        data = self.desglose_completo_ventas_producto()
        if "message" in data:
            return data

        productos = [item[0] for item in data if item[0] is not None]
        ventas = [item[2] for item in data if item[0] is not None]

        plt.figure(figsize=(15, 10))
        plt.bar(productos, ventas, color='blue')
        plt.xlabel('Producto')
        plt.ylabel('Ventas')
        plt.title('Desglose Completo de Ventas por Producto')
        plt.xticks(rotation=10, ha='right')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        return buf

    def get_graphic_venta_farmacia(self):
        data = self.resumen_completo_ventas_farmacia()
        
        payment_methods = {}
        for item in data:
            method = item[2]
            amount = item[3]
            if method not in payment_methods:
                payment_methods[method] = []
            payment_methods[method].append(amount)

        # Calcular el total para cada método de pago
        total_amounts = {}
        for method, amounts in payment_methods.items():
            total_amounts[method] = sum(amounts)

        # Crear el gráfico de barras
        plt.figure(figsize=(12, 10))
        plt.bar(total_amounts.keys(), total_amounts.values(), color='skyblue')
        plt.xlabel('Método de Pago')
        plt.ylabel('Total')
        plt.title('Total de Ventas por Método de Pago')
        plt.xticks(rotation=45)

        # Guardar el gráfico en un buffer de bytes
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        return buf
    
