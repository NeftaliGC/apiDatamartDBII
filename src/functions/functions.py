from src.database.Connection import Connection
from src.database.resumenVentasProducto import ResumenVentasProducto
from src.database.resumenVentasFarmacia import ResumenVentasFarmacia
from src.database.Ranks import Ranks
import matplotlib.pyplot as plt
import io
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Functions:

    def __init__(self):
        self.connection = Connection()

    def connect(self):
        return self.connection.connect()
    #########################################################

    # Funciones para el dense ranking de productos 
    def dense_rank_producto(self, fecha_inicio, fecha_fin):
        self.res = Ranks(fecha_inicio, fecha_fin)
        return self.res.getDenseRank()

    def get_graphic_dense_ranking(self, data):
        buf = self.get_ranking_chart(data)
        return buf

    def dense_rank_completo_producto(self):
        self.res = Ranks()
        return self.res.getDenseRankCompleto()

    def get_graphic_dense_ranking(self, data):
        buf = self.get_ranking_chart(data)
        return buf
    #########################################################

    # Funciones para el ranking de productos
    def rank_producto(self, fecha_inicio, fecha_fin):
        self.res = Ranks(fecha_inicio, fecha_fin, nombre_producto)
        return self.res.getRank()

    def get_graphic_rank_producto(self, fecha_inicio, fecha_fin):
        data = self.rank_producto(fecha_inicio, fecha_fin)
        buf = self.get_ranking_chart(data)

        return buf

    def rank_completo_producto(self):
        self.res = Ranks()
        return self.res.getRankCompleto()

    def get_graphic_rank_completo_producto(self):
        data = self.rank_completo_producto()
        buf = self.get_ranking_chart(data)

        return buf
    #########################################################

    # Funciones para el resumen de ventas por farmacia
    def resumen_ventas_farmacia(self, fecha_inicio, fecha_fin, nombre_farmacia):
        self.res = ResumenVentasFarmacia(fecha_inicio, fecha_fin, nombre_farmacia)
        return self.res.getResumenVentasFarmacia()

    def get_graphic_resumen_ventas_farmacia(self, fecha_inicio, fecha_fin, nombre_farmacia):
        data = self.resumen_ventas_farmacia(fecha_inicio, fecha_fin, nombre_farmacia)
        buf = self.get_pie_chart_for_breakdown(data)

        return buf

    def resumen_completo_ventas_farmacia(self):
        self.res = ResumenVentasFarmacia()
        return self.res.getResumenCompletoVentasFarmacia()

    def get_graphic_venta_farmacia(self):
        data = self.resumen_completo_ventas_farmacia()
        buf = self.get_pie_chart_for_breakdown(data)

        return buf
    #########################################################

    # Funciones para el desglose de ventas por producto
    def desglose_ventas_producto(self, fecha_inicio, fecha_fin, nombre_producto):
        self.res = ResumenVentasProducto(fecha_inicio, fecha_fin, nombre_producto)
        return self.res.getDesgloseVentasProducto()

    def get_graphic_ventas_producto(self, fecha_inicio, fecha_fin, nombre_producto):
        data = self.desglose_ventas_producto(fecha_inicio, fecha_fin, nombre_producto)
        buf = self.get_pie_chart(data)

        return buf

    def desglose_completo_ventas_producto(self):
        self.res = ResumenVentasProducto()
        return self.res.getDesgloseCompletoVentasProducto()

    def get_graphic_desglose_completo(self):
        data = self.desglose_completo_ventas_producto()
        buf = self.get_pie_chart(data)

        return buf
    #########################################################
    
    # Grafico de pastel para desglose
    def get_pie_chart(self, data):
        # Extraer el total general
        total_general = data[0][3]

        # Filtrar los datos para evitar duplicación de subtotales
        ventas_por_categoria = {}
        categoria_producto = {}

        for item in data:
            categoria = item[1]
            venta = item[3]
            producto = item[0]

            if categoria is not None:
                if categoria not in ventas_por_categoria:
                    ventas_por_categoria[categoria] = venta
                    categoria_producto[categoria] = []
                else:
                    # Evitar sumar ventas repetidas en subtotales
                    if venta not in ventas_por_categoria.values():
                        ventas_por_categoria[categoria] += venta

                if producto is not None and producto not in categoria_producto[categoria]:
                    categoria_producto[categoria].append(producto)

        categorias = list(ventas_por_categoria.keys())
        total_ventas = list(ventas_por_categoria.values())

        # Crear etiquetas de leyenda
        legend_labels = []
        for categoria, productos in categoria_producto.items():
            total_ventas_categoria = ventas_por_categoria[categoria]
            legend_labels.append(f"{categoria}: {', '.join(productos)} (${total_ventas_categoria:.2f})")
        legend_labels.append(f"Total General: {total_general:.2f}")

        plt.figure(figsize=(10, 7))
        plt.pie(total_ventas, labels=categorias, autopct='%1.1f%%', startangle=140)
        plt.title('Proporción de Ventas Totales por Categoría')
        plt.axis('equal')
        
        # Agregar la leyenda
        plt.legend(legend_labels, loc='best', bbox_to_anchor=(1, 1))

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        return buf


    #grafico de pastel con desglose para farmacias
    def get_pie_chart_for_breakdown(self, data):
        # Filtrar los datos que tienen método de pago y sumar las ventas por método de pago
        metodos_pago = [item[2] for item in data if item[2] is not None]
        total_ventas = [item[3] for item in data if item[2] is not None]
        
        # Agrupar las ventas por método de pago
        unique_metodos_pago = list(set(metodos_pago))
        ventas_por_metodo = {metodo: 0 for metodo in unique_metodos_pago}
        
        for metodo, venta in zip(metodos_pago, total_ventas):
            ventas_por_metodo[metodo] += venta
        
        labels = list(ventas_por_metodo.keys())
        sizes = list(ventas_por_metodo.values())
        
        # Colores y explosión para destacar los segmentos
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'cyan', 'magenta', 'orange']
        explode = [0.1 if max(sizes) == size else 0 for size in sizes]  # Resalta el mayor segmento
        
        plt.figure(figsize=(15, 12))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Para que el gráfico sea un círculo.
        
        # Añadir leyenda con las farmacias correspondientes
        farmacias = [item[0] for item in data if item[0] is not None]
        metodos_farmacias = [(item[2], item[0]) for item in data if item[0] is not None]
        
        farmacia_por_metodo = {metodo: [] for metodo in unique_metodos_pago}
        
        for metodo, farmacia in metodos_farmacias:
            if farmacia not in farmacia_por_metodo[metodo]:
                farmacia_por_metodo[metodo].append(farmacia)
        
        legend_labels = [f"{metodo}: {', '.join(farmacias)}" for metodo, farmacias in farmacia_por_metodo.items()]
        
        plt.legend(legend_labels, loc="best")
        
        plt.title('Desglose de Ventas por Método de Pago')

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        return buf

    # Grafico de barras para ranking
    def get_ranking_chart(self, data):
        # Ordenar los datos por cantidad vendida
        data_sorted = sorted(data, key=lambda x: x[2], reverse=True)

        productos = [item[1] for item in data_sorted]
        ventas = [item[2] for item in data_sorted]

        plt.figure(figsize=(10, 7))
        plt.barh(productos, ventas, color='skyblue')
        plt.xlabel('Ventas')
        plt.ylabel('Productos')
        plt.title('Ranking de Productos Más Vendidos')
        plt.gca().invert_yaxis()  # Invertir el eje y para que el producto más vendido esté arriba

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        return buf